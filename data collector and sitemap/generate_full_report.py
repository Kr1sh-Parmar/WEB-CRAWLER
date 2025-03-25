import pandas as pd
import os
import matplotlib.pyplot as plt
import json
from datetime import datetime
import base64
import io
from urllib.parse import urlparse

def create_chart_image(plt_figure):
    """Convert a matplotlib figure to a base64 encoded string for HTML embedding"""
    buf = io.BytesIO()
    plt_figure.savefig(buf, format='png', dpi=100)
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{img_str}"

def generate_content_type_chart(pages_df):
    """Generate content type distribution chart"""
    plt.figure(figsize=(10, 6))
    content_types = pages_df['Content Type'].value_counts()
    content_types.plot(kind='bar')
    plt.title('Content Types Distribution')
    plt.xlabel('Content Type')
    plt.ylabel('Number of Pages')
    plt.tight_layout()
    return plt.gcf()

def generate_domains_chart(pages_df):
    """Generate domains distribution chart"""
    domains = []
    for url in pages_df['URL']:
        parsed = urlparse(url)
        domains.append(parsed.netloc)
    
    domain_counts = pd.Series(domains).value_counts()
    
    plt.figure(figsize=(10, 6))
    domain_counts.head(10).plot(kind='bar')
    plt.title('Top 10 Domains')
    plt.xlabel('Domain')
    plt.ylabel('Number of Pages')
    plt.tight_layout()
    return plt.gcf()

def generate_report():
    """Generate a comprehensive HTML report"""
    data_dir = "mosdac_full_data"
    report_path = os.path.join(data_dir, "comprehensive_report.html")
    
    # Check if data directory exists
    if not os.path.exists(data_dir):
        print(f"Error: Data directory '{data_dir}' not found!")
        return
    
    print("Reading data files...")
    
    # Read CSV files
    pages_df = pd.read_csv(os.path.join(data_dir, "all_pages.csv"))
    data_files_df = pd.read_csv(os.path.join(data_dir, "data_files.csv"))
    
    # Generate charts
    print("Generating charts...")
    content_type_chart = create_chart_image(generate_content_type_chart(pages_df))
    domains_chart = create_chart_image(generate_domains_chart(pages_df))
    
    # Calculate statistics
    total_pages = len(pages_df)
    total_files = len(data_files_df)
    file_types = data_files_df['Type'].value_counts().to_dict()
    
    # Top pages by links
    top_linked_pages = pages_df.sort_values('Links Count', ascending=False).head(10)
    
    # Top pages by images
    top_image_pages = pages_df.sort_values('Images Count', ascending=False).head(10)
    
    # Generate HTML
    print("Generating HTML report...")
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>MOSDAC Website Comprehensive Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; line-height: 1.6; color: #333; }}
        h1, h2, h3 {{ color: #205493; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .chart {{ margin: 20px 0; text-align: center; }}
        .chart img {{ max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; }}
        table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
        th {{ background-color: #f2f2f2; position: sticky; top: 0; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
        .stats-container {{ display: flex; flex-wrap: wrap; gap: 20px; margin: 20px 0; }}
        .stat-card {{ flex: 1; min-width: 200px; padding: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        .stat-value {{ font-size: 32px; font-weight: bold; margin: 10px 0; }}
        .blue {{ background-color: #e1f3f8; }}
        .green {{ background-color: #e7f4e4; }}
        .yellow {{ background-color: #fff1d2; }}
        footer {{ margin-top: 50px; border-top: 1px solid #ddd; padding-top: 20px; color: #666; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>MOSDAC Website Comprehensive Report</h1>
        <p>Report generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}</p>
        
        <section>
            <h2>Overview Statistics</h2>
            
            <div class="stats-container">
                <div class="stat-card blue">
                    <h3>Total Pages</h3>
                    <div class="stat-value">{total_pages}</div>
                </div>
                
                <div class="stat-card green">
                    <h3>Data Files</h3>
                    <div class="stat-value">{total_files}</div>
                </div>
                
                <div class="stat-card yellow">
                    <h3>File Types</h3>
                    <div class="stat-value">{len(file_types)}</div>
                </div>
            </div>
        </section>
        
        <section>
            <h2>Content Distribution</h2>
            
            <div class="chart">
                <h3>Content Types Distribution</h3>
                <img src="{content_type_chart}" alt="Content Types Distribution">
            </div>
            
            <div class="chart">
                <h3>Domains Distribution</h3>
                <img src="{domains_chart}" alt="Domains Distribution">
            </div>
        </section>
        
        <section>
            <h2>Top Pages by Links</h2>
            <table>
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>URL</th>
                        <th>Links</th>
                    </tr>
                </thead>
                <tbody>
                """
    
    for _, row in top_linked_pages.iterrows():
        html_content += f"""
                    <tr>
                        <td>{row['Title']}</td>
                        <td><a href="{row['URL']}" target="_blank">{row['URL']}</a></td>
                        <td>{row['Links Count']}</td>
                    </tr>"""
    
    html_content += """
                </tbody>
            </table>
        </section>
        
        <section>
            <h2>Top Pages by Images</h2>
            <table>
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>URL</th>
                        <th>Images</th>
                    </tr>
                </thead>
                <tbody>
                """
    
    for _, row in top_image_pages.iterrows():
        html_content += f"""
                    <tr>
                        <td>{row['Title']}</td>
                        <td><a href="{row['URL']}" target="_blank">{row['URL']}</a></td>
                        <td>{row['Images Count']}</td>
                    </tr>"""
    
    html_content += """
                </tbody>
            </table>
        </section>
        
        <section>
            <h2>Available Data Files</h2>
            <table>
                <thead>
                    <tr>
                        <th>Filename</th>
                        <th>Type</th>
                        <th>URL</th>
                    </tr>
                </thead>
                <tbody>
                """
    
    # List unique files by name
    unique_files = {}
    for _, row in data_files_df.iterrows():
        if row['Filename'] not in unique_files:
            unique_files[row['Filename']] = row
    
    for filename, row in unique_files.items():
        html_content += f"""
                    <tr>
                        <td>{row['Filename']}</td>
                        <td>{row['Type']}</td>
                        <td><a href="{row['URL']}" target="_blank">Download</a></td>
                    </tr>"""
    
    html_content += """
                </tbody>
            </table>
        </section>
        
        <section>
            <h2>Next Steps</h2>
            <ul>
                <li>Use the <code>download_mosdac_files.py</code> script to download specific data files.</li>
                <li>Explore the sitemap visualization in <code>sitemap_visual.png</code> to understand the website structure.</li>
                <li>Check the raw CSV files for more detailed information.</li>
                <li>Review individual pages stored in the <code>pages</code> directory.</li>
            </ul>
        </section>
        
        <footer>
            <p>Report generated by MOSDAC Website Crawler Analysis Tools</p>
        </footer>
    </div>
</body>
</html>
    """
    
    # Write the HTML report
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Comprehensive report generated at: {os.path.abspath(report_path)}")

if __name__ == "__main__":
    print("Generating comprehensive MOSDAC website report...")
    generate_report()
    print("Done!") 