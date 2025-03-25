import requests
from bs4 import BeautifulSoup
import time
import csv
import os
import json
from urllib.parse import urljoin, urlparse
import threading
from queue import Queue
import logging
from datetime import datetime

class MOSDACFullWebsiteCrawler:
    def __init__(self, base_url, delay=1.0, output_dir="mosdac_full_data", num_threads=4, max_retries=3):
        """
        Initialize the MOSDAC full website crawler with multithreading support.
        
        Args:
            base_url (str): The base URL of the MOSDAC website.
            delay (float): Delay between requests in seconds to avoid overloading the server.
            output_dir (str): Directory to save crawled data.
            num_threads (int): Number of concurrent threads for crawling.
            max_retries (int): Maximum number of retries for failed requests.
        """
        self.base_url = base_url
        self.delay = delay
        self.output_dir = output_dir
        self.num_threads = num_threads
        self.max_retries = max_retries
        
        # Threading and synchronization
        self.url_queue = Queue()
        self.url_queue.put(base_url)
        self.visited_urls = set()
        self.url_lock = threading.Lock()
        self.data_lock = threading.Lock()
        
        # Setup logging
        log_dir = os.path.join(output_dir, "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        logging.basicConfig(
            filename=os.path.join(log_dir, f'crawler_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # Create output directories
        self.setup_directories()
        
        # Initialize data storage
        self.initialize_data_files()
        
        # Stats tracking
        self.stats = {
            'pages_crawled': 0,
            'errors': 0,
            'start_time': time.time(),
            'data_files_found': 0,
            'images_found': 0
        }
    
    def setup_directories(self):
        """Create all necessary directories for storing crawled data."""
        dirs = [
            self.output_dir,
            os.path.join(self.output_dir, "pages"),
            os.path.join(self.output_dir, "data"),
            os.path.join(self.output_dir, "images"),
            os.path.join(self.output_dir, "metadata")
        ]
        
        for directory in dirs:
            if not os.path.exists(directory):
                os.makedirs(directory)
    
    def initialize_data_files(self):
        """Initialize CSV and JSON files for storing crawler data."""
        # Main data CSV file
        self.pages_csv = os.path.join(self.output_dir, "all_pages.csv")
        with open(self.pages_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['URL', 'Title', 'Content Type', 'Links Count', 'Images Count', 'Last Modified', 'Status'])
        
        # Data files CSV
        self.data_files_csv = os.path.join(self.output_dir, "data_files.csv")
        with open(self.data_files_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['URL', 'Filename', 'Type', 'Size', 'Description'])
        
        # Products CSV
        self.products_csv = os.path.join(self.output_dir, "satellite_products.csv")
        with open(self.products_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['URL', 'Product Name', 'Description', 'Data Format', 'Source'])
        
        # Sitemap JSON
        self.sitemap_json = os.path.join(self.output_dir, "sitemap.json")
        with open(self.sitemap_json, 'w', encoding='utf-8') as f:
            json.dump({"base_url": self.base_url, "pages": {}}, f)
    
    def is_valid_url(self, url):
        """Check if URL belongs to the same domain and hasn't been visited yet."""
        try:
            parsed_base = urlparse(self.base_url)
            parsed_url = urlparse(url)
            
            # Check if this is a valid URL and belongs to the same domain
            return (parsed_url.netloc == parsed_base.netloc or 
                    (parsed_url.netloc == '' and parsed_url.path and not parsed_url.path.startswith('#')))
        except:
            return False
    
    def normalize_url(self, url):
        """Normalize URL by removing fragments and standardizing format."""
        parsed = urlparse(url)
        normalized = parsed._replace(fragment='').geturl()
        # Remove trailing slash for consistency
        if normalized.endswith('/') and normalized != self.base_url:
            normalized = normalized[:-1]
        return normalized
    
    def save_page_content(self, url, content):
        """Save the raw HTML content of a page."""
        try:
            parsed_url = urlparse(url)
            path_parts = parsed_url.path.strip('/').split('/')
            
            # Create a filename based on the URL
            if not path_parts or path_parts[0] == '':
                filename = "index"
            else:
                filename = '_'.join(path_parts)
                
            if parsed_url.query:
                filename += '_' + parsed_url.query.replace('=', '_').replace('&', '_')
            
            filename = filename.replace('.', '_')
            if not filename.endswith(".html"):
                filename += ".html"
            
            # Ensure filename length is reasonable
            if len(filename) > 200:
                filename = filename[:200] + ".html"
            
            file_path = os.path.join(self.output_dir, "pages", filename)
            with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
                f.write(content)
            
            return filename
        except Exception as e:
            logging.error(f"Error saving page content for {url}: {e}")
            return None
    
    def detect_content_type(self, url, soup):
        """Detect the content type of a page based on URL and content."""
        url_lower = url.lower()
        
        # Check specific paths or keywords in URL
        if "/data/" in url_lower:
            return "Data Repository"
        elif "/product" in url_lower:
            return "Product Page"
        elif "/about" in url_lower:
            return "About Page"
        elif "/contact" in url_lower:
            return "Contact Page"
        elif "/download" in url_lower:
            return "Download Page"
        
        # Check page content
        if soup.find("form"):
            return "Form Page"
        
        # Check page title
        title = soup.title.text.lower() if soup.title else ""
        if "data" in title:
            return "Data Page"
        elif "product" in title:
            return "Product Page"
        elif "download" in title:
            return "Download Page"
        elif "about" in title:
            return "About Page"
        
        # Default
        return "General Page"
    
    def extract_page_metadata(self, url, soup, response):
        """Extract metadata from a page."""
        try:
            title = soup.title.text.strip() if soup.title else "No Title"
            content_type = self.detect_content_type(url, soup)
            
            # Count links and images
            links = soup.find_all('a', href=True)
            links_count = len(links)
            
            images = soup.find_all('img', src=True)
            images_count = len(images)
            
            # Get last modified date if available
            last_modified = response.headers.get('Last-Modified', 'Unknown')
            
            with self.data_lock:
                with open(self.pages_csv, 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([url, title, content_type, links_count, images_count, last_modified, response.status_code])
            
            return {
                'url': url,
                'title': title,
                'content_type': content_type,
                'links_count': links_count,
                'images_count': images_count,
                'last_modified': last_modified
            }
        
        except Exception as e:
            logging.error(f"Error extracting metadata for {url}: {e}")
            return None
    
    def find_data_files(self, url, soup):
        """Find and record data files linked from the page."""
        try:
            # Look for links to data files
            data_extensions = ['.dat', '.nc', '.h5', '.hdf', '.hdf5', '.zip', '.tar', '.gz', '.tgz', '.csv', '.txt']
            
            data_files = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                if any(href.lower().endswith(ext) for ext in data_extensions):
                    full_url = urljoin(url, href)
                    
                    # Get description if available
                    description = link.get_text().strip()
                    if not description:
                        description = link.get('title', 'No description')
                    
                    # Get file type
                    file_type = href.split('.')[-1].upper()
                    
                    data_files.append({
                        'url': full_url,
                        'filename': href.split('/')[-1],
                        'type': file_type,
                        'size': 'Unknown',
                        'description': description
                    })
            
            if data_files:
                with self.data_lock:
                    with open(self.data_files_csv, 'a', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        for data_file in data_files:
                            writer.writerow([
                                data_file['url'],
                                data_file['filename'],
                                data_file['type'],
                                data_file['size'],
                                data_file['description']
                            ])
                    
                    self.stats['data_files_found'] += len(data_files)
            
            return data_files
        
        except Exception as e:
            logging.error(f"Error finding data files on {url}: {e}")
            return []
    
    def extract_satellite_products(self, url, soup):
        """Extract information about satellite data products."""
        try:
            # This is highly specific to the website structure
            # Look for products in various ways
            products = []
            
            # Method 1: Look for specific product containers
            product_containers = soup.find_all(['div', 'section'], class_=lambda c: c and ('product' in c.lower() or 'dataset' in c.lower()))
            
            for container in product_containers:
                # Try to find name, description, and other details
                name_elem = container.find(['h2', 'h3', 'h4', 'strong'])
                name = name_elem.get_text().strip() if name_elem else "Unknown Product"
                
                desc_elem = container.find('p')
                description = desc_elem.get_text().strip() if desc_elem else "No description available"
                
                # Look for data format if available
                format_elem = container.find(text=lambda t: t and ('format' in t.lower() or 'type' in t.lower()))
                data_format = format_elem.find_next().get_text().strip() if format_elem and format_elem.find_next() else "Unknown"
                
                # Look for source satellite
                source_elem = container.find(text=lambda t: t and ('satellite' in t.lower() or 'instrument' in t.lower()))
                source = source_elem.find_next().get_text().strip() if source_elem and source_elem.find_next() else "Unknown"
                
                products.append({
                    'url': url,
                    'name': name,
                    'description': description,
                    'data_format': data_format,
                    'source': source
                })
            
            # Method 2: Look for tables containing product information
            tables = soup.find_all('table')
            for table in tables:
                headers = [th.get_text().strip().lower() for th in table.find_all('th')]
                
                # Check if this might be a product table
                product_table = any(h in ['product', 'dataset', 'data product'] for h in headers)
                
                if product_table:
                    for row in table.find_all('tr')[1:]:  # Skip header row
                        cells = row.find_all(['td', 'th'])
                        if len(cells) >= 2:
                            product = {
                                'url': url,
                                'name': cells[0].get_text().strip(),
                                'description': cells[1].get_text().strip() if len(cells) > 1 else "No description",
                                'data_format': cells[2].get_text().strip() if len(cells) > 2 else "Unknown",
                                'source': cells[3].get_text().strip() if len(cells) > 3 else "Unknown"
                            }
                            products.append(product)
            
            if products:
                with self.data_lock:
                    with open(self.products_csv, 'a', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        for product in products:
                            writer.writerow([
                                product['url'],
                                product['name'],
                                product['description'],
                                product['data_format'],
                                product['source']
                            ])
            
            return products
        
        except Exception as e:
            logging.error(f"Error extracting satellite products from {url}: {e}")
            return []
    
    def update_sitemap(self, url, links):
        """Update the sitemap JSON file with new links."""
        try:
            with self.data_lock:
                # Load current sitemap
                with open(self.sitemap_json, 'r', encoding='utf-8') as f:
                    sitemap = json.load(f)
                
                # Add this page and its links
                sitemap["pages"][url] = [link for link in links if self.is_valid_url(link)]
                
                # Save updated sitemap
                with open(self.sitemap_json, 'w', encoding='utf-8') as f:
                    json.dump(sitemap, f, indent=2)
        
        except Exception as e:
            logging.error(f"Error updating sitemap for {url}: {e}")
    
    def worker(self):
        """Worker thread function for concurrent crawling."""
        while True:
            # Get next URL from the queue
            url = self.url_queue.get()
            
            # Check if we've already visited this URL
            with self.url_lock:
                if url in self.visited_urls:
                    self.url_queue.task_done()
                    continue
                
                # Mark as visited before processing
                self.visited_urls.add(url)
            
            # Process the URL
            self.process_url(url)
            
            # Mark task as done
            self.url_queue.task_done()
    
    def process_url(self, url):
        """Process a single URL: fetch content, extract links, and analyze."""
        for attempt in range(self.max_retries):
            try:
                logging.info(f"Crawling: {url}")
                
                # Send request with headers
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Referer': self.base_url
                }
                
                response = requests.get(url, headers=headers, timeout=20)
                
                if response.status_code == 200:
                    # Parse the HTML content
                    content_type = response.headers.get('Content-Type', '').lower()
                    
                    if 'text/html' in content_type:
                        # Process HTML page
                        soup = BeautifulSoup(response.text, 'html.parser')
                        
                        # Save raw HTML
                        self.save_page_content(url, response.text)
                        
                        # Extract page metadata
                        self.extract_page_metadata(url, soup, response)
                        
                        # Find data files
                        self.find_data_files(url, soup)
                        
                        # Extract product information
                        self.extract_satellite_products(url, soup)
                        
                        # Find all links on the page
                        links = []
                        for link in soup.find_all('a', href=True):
                            href = link['href']
                            full_url = urljoin(url, href)
                            
                            # Normalize and validate URL
                            full_url = self.normalize_url(full_url)
                            
                            if self.is_valid_url(full_url):
                                links.append(full_url)
                                
                                # Add to queue if not visited
                                with self.url_lock:
                                    if full_url not in self.visited_urls:
                                        self.url_queue.put(full_url)
                        
                        # Update sitemap
                        self.update_sitemap(url, links)
                        
                        # Update stats
                        with self.data_lock:
                            self.stats['pages_crawled'] += 1
                            
                            # Print progress every 10 pages
                            if self.stats['pages_crawled'] % 10 == 0:
                                elapsed = time.time() - self.stats['start_time']
                                print(f"Progress: {self.stats['pages_crawled']} pages crawled in {elapsed:.1f} seconds")
                    
                    # Wait to be respectful
                    time.sleep(self.delay)
                    
                    # Successfully processed
                    break
                
                elif response.status_code in [429, 503]:
                    # Rate limited or service unavailable, wait longer and retry
                    logging.warning(f"Rate limited on {url}. Waiting before retry.")
                    time.sleep(self.delay * 5)  # Longer delay before retry
                
                else:
                    # Log non-200 responses
                    logging.warning(f"Non-200 response for {url}: {response.status_code}")
                    break
            
            except Exception as e:
                logging.error(f"Error processing {url} (attempt {attempt+1}/{self.max_retries}): {e}")
                with self.data_lock:
                    self.stats['errors'] += 1
                
                # Wait before retry
                time.sleep(self.delay * 2)
    
    def crawl(self):
        """
        Start crawling the entire website using multiple threads.
        """
        print(f"Starting full website crawl of {self.base_url} with {self.num_threads} threads")
        print(f"Data will be saved to: {os.path.abspath(self.output_dir)}")
        
        # Create and start worker threads
        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.worker, daemon=True)
            thread.start()
            threads.append(thread)
        
        # Wait for all URLs to be processed
        try:
            # Check progress periodically
            while True:
                queue_size = self.url_queue.qsize()
                visited_count = len(self.visited_urls)
                
                if queue_size == 0 and visited_count > 0:
                    # Double check there are no items in processing
                    time.sleep(5)
                    if self.url_queue.qsize() == 0:
                        break
                
                # Print status
                elapsed = time.time() - self.stats['start_time']
                print(f"Status: {visited_count} pages visited, {queue_size} in queue, {self.stats['errors']} errors, {elapsed:.1f} seconds elapsed")
                
                time.sleep(10)  # Check every 10 seconds
            
            # Wait for queue to be fully processed
            self.url_queue.join()
        
        except KeyboardInterrupt:
            print("\nCrawl interrupted by user.")
        
        # Print final stats
        self.print_stats()
        
        # Generate final report
        self.generate_report()
        
        return self.stats
    
    def print_stats(self):
        """Print crawler statistics."""
        elapsed = time.time() - self.stats['start_time']
        
        print("\n" + "=" * 50)
        print("MOSDAC Website Crawler - Complete")
        print("=" * 50)
        print(f"Total pages crawled: {self.stats['pages_crawled']}")
        print(f"Total errors: {self.stats['errors']}")
        print(f"Data files found: {self.stats['data_files_found']}")
        print(f"Total time: {elapsed:.1f} seconds")
        if self.stats['pages_crawled'] > 0:
            print(f"Average time per page: {elapsed/self.stats['pages_crawled']:.2f} seconds")
        print("=" * 50)
    
    def generate_report(self):
        """Generate a summary report of the crawl."""
        report_path = os.path.join(self.output_dir, "crawl_report.html")
        
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(f"""<!DOCTYPE html>
<html>
<head>
    <title>MOSDAC Website Crawl Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1, h2 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
        .stats {{ display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 20px; }}
        .stat-card {{ border: 1px solid #ddd; border-radius: 5px; padding: 15px; flex: 1; min-width: 200px; }}
        .stat-value {{ font-size: 24px; font-weight: bold; margin: 10px 0; }}
    </style>
</head>
<body>
    <h1>MOSDAC Website Crawl Report</h1>
    <p>Crawl completed on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    
    <div class="stats">
        <div class="stat-card">
            <h3>Pages Crawled</h3>
            <div class="stat-value">{self.stats['pages_crawled']}</div>
        </div>
        <div class="stat-card">
            <h3>Data Files Found</h3>
            <div class="stat-value">{self.stats['data_files_found']}</div>
        </div>
        <div class="stat-card">
            <h3>Errors</h3>
            <div class="stat-value">{self.stats['errors']}</div>
        </div>
        <div class="stat-card">
            <h3>Time Elapsed</h3>
            <div class="stat-value">{(time.time() - self.stats['start_time']):.1f}s</div>
        </div>
    </div>
    
    <h2>Content Summary</h2>
    <p>The following data files were collected during the crawl:</p>
    
    <ul>
        <li><a href="all_pages.csv">Complete list of pages</a></li>
        <li><a href="data_files.csv">Data files</a></li>
        <li><a href="satellite_products.csv">Satellite products</a></li>
        <li><a href="sitemap.json">Site structure map</a></li>
    </ul>
    
    <h2>Next Steps</h2>
    <p>To analyze the collected data:</p>
    <ol>
        <li>Review the CSV files to find specific data products</li>
        <li>Examine the pages directory for archived HTML content</li>
        <li>Use the sitemap to understand the website structure</li>
    </ol>
</body>
</html>""")
            
            print(f"Report generated: {os.path.abspath(report_path)}")
        
        except Exception as e:
            logging.error(f"Error generating report: {e}")

# Example usage
if __name__ == "__main__":
    crawler = MOSDACFullWebsiteCrawler(
        base_url="https://www.mosdac.gov.in/",
        delay=1.0,  # 1 second delay between requests
        output_dir="mosdac_full_data",
        num_threads=4  # Using 4 threads for parallel crawling
    )
    
    crawler.crawl()
