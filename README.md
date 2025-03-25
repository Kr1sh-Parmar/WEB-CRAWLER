# WEB-CRAWLER

# ISRO MOSDAC Website Crawler

This project is a web crawler designed to scrape data from the [MOSDAC (Meteorological and Oceanographic Satellite Data Archival Centre)](https://www.mosdac.gov.in/) website. It extracts useful information such as pages, data files, and satellite products, stores the data in structured formats, and provides analysis and visualization.

## Features
- **Multithreaded Crawling**: Efficiently crawls the entire MOSDAC website.
- **Data Extraction**: Extracts metadata, links, and satellite product details.
- **Data Conversion**: Converts HTML pages into structured JSON format.
- **Visualization**: Generates a sitemap and content distribution graphs.
- **Download Support**: Facilitates downloading of available data files.
- **Comprehensive Reports**: Creates detailed reports with statistical insights.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- Required dependencies (install using `requirements.txt`)

### Setup
Clone the repository and install dependencies:
```bash
# Clone the repository
git clone https://github.com/yourusername/mosdac-web-crawler.git
cd mosdac-web-crawler

# Install dependencies
pip install -r requirements.txt
```

## Usage
### Running the Web Crawler
To start crawling the MOSDAC website, run:
```bash
python mosdac-full-website-crawler.py
```

### Convert HTML to JSON
To convert scraped HTML files into structured JSON, use:
```bash
python converter.py
```

### Analyze the Crawled Data
To generate statistics and content analysis:
```bash
python analyze_mosdac_data.py
```

### Generate Sitemap Visualization
To create a visual representation of the crawled pages:
```bash
python create_sitemap_visual.py
```

### Download Data Files
To download available datasets:
```bash
python download_mosdac_files.py
```

### Generate Full Report
To generate a detailed HTML report:
```bash
python generate_full_report.py
```

## Project Structure
```
mosdac-web-crawler/
├── converter.py              # Converts HTML to JSON
├── analyze_mosdac_data.py    # Analyzes crawled data
├── create_sitemap_visual.py  # Generates website sitemap visualization
├── download_mosdac_files.py  # Downloads available MOSDAC datasets
├── generate_full_report.py   # Creates an HTML-based comprehensive report
├── mosdac-full-website-crawler.py  # The main web crawler script
├── requirements.txt          # Dependencies list
├── README.md                 # Project documentation
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Create a Pull Request.



## Author
Developed by KRISH. If you have any questions or suggestions, feel free to reach out!

