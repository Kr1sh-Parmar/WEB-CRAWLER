import os
import json
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup

def select_folder(purpose):
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title=f"Select {purpose} Folder")
    root.destroy()
    return folder

def html_to_json_converter():
    # Get folders through GUI
    input_folder = select_folder("HTML Input")
    if not input_folder:
        print("No input folder selected. Exiting.")
        return

    output_folder = select_folder("JSON Output")
    if not output_folder:
        print("No output folder selected. Exiting.")
        return

    # Create output directory if needed
    os.makedirs(output_folder, exist_ok=True)

    # Get all HTML files
    html_files = [f for f in os.listdir(input_folder) if f.endswith('.html')]
    total_files = len(html_files)
    
    print(f"Found {total_files} HTML files in {input_folder}")
    print(f"Converting to JSON in {output_folder}...")

    for index, filename in enumerate(html_files):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.json")

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'lxml')
                
            # Create structured JSON
            json_data = {
                "metadata": {
                    "source": filename,
                    "path": input_path
                },
                "content": {
                    "headers": [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])],
                    "paragraphs": [p.get_text() for p in soup.find_all('p')],
                    "links": [a['href'] for a in soup.find_all('a', href=True)]
                }
            }

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2)

            # Update progress
            progress = (index + 1) / total_files * 100
            print(f"Processed: {index + 1}/{total_files} ({progress:.1f}%) - {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

    print("Conversion complete!")

if __name__ == "__main__":
    html_to_json_converter()
