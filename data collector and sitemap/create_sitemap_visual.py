import pandas as pd
import os
import networkx as nx
import matplotlib.pyplot as plt
from urllib.parse import urlparse
import json

def create_visual_sitemap():
    # Set path to the crawled data
    data_dir = "mosdac_full_data"
    pages_csv = os.path.join(data_dir, "all_pages.csv")
    
    # Check if file exists
    if not os.path.exists(pages_csv):
        print(f"Error: File not found: {pages_csv}")
        return
    
    # Read the all_pages.csv file
    print("Reading pages data...")
    pages_df = pd.read_csv(pages_csv)
    
    # Extract unique domains and paths
    print("Extracting domains and paths...")
    domains = []
    paths = []
    
    for url in pages_df['URL']:
        parsed = urlparse(url)
        domain = parsed.netloc
        path_parts = parsed.path.strip('/').split('/')
        
        domains.append(domain)
        
        # Add each path segment
        current_path = ''
        for part in path_parts:
            if part:
                current_path = current_path + '/' + part if current_path else '/' + part
                paths.append((domain, current_path))
    
    # Count unique domains
    unique_domains = set(domains)
    print(f"Found {len(unique_domains)} unique domains")
    
    # Create a graph
    print("Creating site map graph...")
    G = nx.DiGraph()
    
    # Add domain nodes
    for domain in unique_domains:
        G.add_node(domain, type='domain')
    
    # Add path nodes and edges
    added_paths = set()
    for domain, path in paths:
        if (domain, path) not in added_paths:
            G.add_node(f"{domain}{path}", type='path')
            
            # Connect to parent
            parent_path = os.path.dirname(path)
            if parent_path and parent_path != '/':
                G.add_edge(f"{domain}{parent_path}", f"{domain}{path}")
            else:
                G.add_edge(domain, f"{domain}{path}")
            
            added_paths.add((domain, path))
    
    # Draw basic graph (this may be large)
    print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    
    # For very large sites, we'll create a simplified visualization
    if G.number_of_nodes() > 100:
        print("Creating simplified site map (too many nodes for detailed view)...")
        
        # Group by first path segment
        top_level_paths = {}
        for domain, path in added_paths:
            if path.count('/') == 1:  # Top-level paths only
                path_name = path.strip('/')
                if path_name not in top_level_paths:
                    top_level_paths[path_name] = 0
                top_level_paths[path_name] += 1
        
        # Create a simplified graph
        SG = nx.DiGraph()
        
        # Add the main domain
        main_domain = list(unique_domains)[0]  # Assuming one main domain
        SG.add_node(main_domain, type='domain')
        
        # Add top-level sections as nodes
        for path, count in top_level_paths.items():
            if path:  # Skip empty paths
                SG.add_node(path, type='section', count=count)
                SG.add_edge(main_domain, path)
        
        # Draw the simplified graph
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(SG, seed=42)
        
        # Node colors based on type
        node_colors = ['skyblue' if SG.nodes[n]['type'] == 'domain' else 'lightgreen' for n in SG.nodes]
        
        # Node sizes based on count (for sections)
        node_sizes = [1000 if SG.nodes[n]['type'] == 'domain' else 
                      300 + (SG.nodes[n].get('count', 1) * 5) for n in SG.nodes]
        
        nx.draw(SG, pos, with_labels=True, node_color=node_colors, 
                node_size=node_sizes, font_size=8, arrows=True)
        
        plt.title(f"MOSDAC Website Structure - Top-Level Sections")
        plt.savefig(os.path.join(data_dir, "sitemap_visual.png"), dpi=300, bbox_inches='tight')
        print(f"Simplified site map saved to {os.path.join(data_dir, 'sitemap_visual.png')}")
    else:
        # Draw full graph for smaller sites
        plt.figure(figsize=(15, 10))
        pos = nx.spring_layout(G, seed=42)
        
        # Node colors based on type
        node_colors = ['skyblue' if G.nodes[n]['type'] == 'domain' else 'lightgreen' for n in G.nodes]
        
        nx.draw(G, pos, with_labels=True, node_color=node_colors, 
                node_size=500, font_size=8, arrows=True)
        
        plt.title(f"MOSDAC Website Structure - Full Map")
        plt.savefig(os.path.join(data_dir, "sitemap_visual.png"), dpi=300, bbox_inches='tight')
        print(f"Full site map saved to {os.path.join(data_dir, 'sitemap_visual.png')}")

if __name__ == "__main__":
    print("Creating visual sitemap from crawled data...")
    create_visual_sitemap()
    print("Done!") 