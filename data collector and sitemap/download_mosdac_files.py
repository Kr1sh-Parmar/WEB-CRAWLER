import pandas as pd
import os
import requests
from tqdm import tqdm

def download_file(url, destination):
    """Download a file from a URL to a specified destination with progress bar"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Get file size for progress bar
        total_size = int(response.headers.get('content-length', 0))
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        
        # Download with progress bar
        with open(destination, 'wb') as file, tqdm(
                desc=os.path.basename(destination),
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    bar.update(len(chunk))
        
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def main():
    # Set paths
    data_dir = "mosdac_full_data"
    download_dir = "mosdac_downloads"
    
    # Create download directory if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)
    
    # Read the data files CSV
    data_files_df = pd.read_csv(os.path.join(data_dir, "data_files.csv"))
    
    # Display available files
    print(f"Found {len(data_files_df)} files available for download:")
    for i, (_, row) in enumerate(data_files_df.iterrows(), 1):
        print(f"{i}. {row['Filename']} ({row['Type']})")
    
    # Ask user which files to download
    print("\nEnter the numbers of the files you want to download (comma-separated), or 'all' for all files:")
    choice = input("> ")
    
    files_to_download = []
    if choice.lower() == 'all':
        files_to_download = list(range(len(data_files_df)))
    else:
        try:
            selected = [int(x.strip()) - 1 for x in choice.split(',')]
            files_to_download = [i for i in selected if 0 <= i < len(data_files_df)]
        except:
            print("Invalid input. Please run the script again.")
            return
    
    # Download selected files
    if not files_to_download:
        print("No valid files selected.")
        return
    
    print(f"\nDownloading {len(files_to_download)} files...")
    
    successful = 0
    for i in files_to_download:
        row = data_files_df.iloc[i]
        url = row['URL']
        filename = row['Filename']
        destination = os.path.join(download_dir, filename)
        
        print(f"\nDownloading {filename} from {url}")
        if download_file(url, destination):
            successful += 1
    
    print(f"\nDownload complete! Successfully downloaded {successful} of {len(files_to_download)} files.")
    print(f"Files saved to: {os.path.abspath(download_dir)}")

if __name__ == "__main__":
    main() 