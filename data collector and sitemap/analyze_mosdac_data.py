import pandas as pd
import os
import matplotlib.pyplot as plt
from collections import Counter

# Set the path to the crawled data
data_dir = "mosdac_full_data"

# Function to analyze the crawled pages
def analyze_pages():
    print("Analyzing crawled pages...")
    
    # Read the all_pages.csv file
    pages_df = pd.read_csv(os.path.join(data_dir, "all_pages.csv"))
    
    # Basic statistics
    total_pages = len(pages_df)
    print(f"Total pages crawled: {total_pages}")
    
    # Content type analysis
    content_types = pages_df['Content Type'].value_counts()
    print("\nContent Types:")
    for content_type, count in content_types.items():
        print(f"  - {content_type}: {count} pages ({count/total_pages*100:.1f}%)")
    
    # Pages with most links
    top_linked_pages = pages_df.sort_values('Links Count', ascending=False).head(10)
    print("\nTop 10 Pages with Most Links:")
    for _, row in top_linked_pages.iterrows():
        print(f"  - {row['Title']} ({row['URL']}): {row['Links Count']} links")
    
    # Pages with most images
    top_image_pages = pages_df.sort_values('Images Count', ascending=False).head(10)
    print("\nTop 10 Pages with Most Images:")
    for _, row in top_image_pages.iterrows():
        print(f"  - {row['Title']} ({row['URL']}): {row['Images Count']} images")
    
    # Create visualizations
    try:
        plt.figure(figsize=(10, 6))
        content_types.plot(kind='bar')
        plt.title('Content Types Distribution')
        plt.xlabel('Content Type')
        plt.ylabel('Number of Pages')
        plt.tight_layout()
        plt.savefig(os.path.join(data_dir, "content_types.png"))
        print(f"\nContent types chart saved to {os.path.join(data_dir, 'content_types.png')}")
    except Exception as e:
        print(f"Error creating visualization: {e}")

# Function to analyze data files
def analyze_data_files():
    print("\nAnalyzing data files...")
    
    # Read the data_files.csv file
    data_files_df = pd.read_csv(os.path.join(data_dir, "data_files.csv"))
    
    # Basic statistics
    total_files = len(data_files_df)
    print(f"Total data files found: {total_files}")
    
    # File type analysis
    file_types = data_files_df['Type'].value_counts()
    print("\nFile Types:")
    for file_type, count in file_types.items():
        print(f"  - {file_type}: {count} files ({count/total_files*100:.1f}%)")

# Main function
def main():
    print("MOSDAC Crawler Data Analysis")
    print("=" * 30)
    
    # Check if the data directory exists
    if not os.path.exists(data_dir):
        print(f"Error: Data directory '{data_dir}' not found!")
        return
    
    # Run analysis functions
    analyze_pages()
    analyze_data_files()
    
    print("\nAnalysis complete!")
    print("You can use this information to decide which parts of the data to explore further.")

if __name__ == "__main__":
    main() 