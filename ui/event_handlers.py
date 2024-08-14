import os
import requests
import tkinter as tk
from tkinter import messagebox
from ui.data_display import display_data
from config.config import API_KEY
from api.fetcher import fetch_alphafold_data
import subprocess

def download_file(url, save_path):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    with open(save_path, 'wb') as file:
        file.write(response.content)

def open_files(pdb_path, cif_path, bcif_path, png_path):
    # Open molecular structure files in PyMOL
    subprocess.Popen(['pymol', pdb_path])
    subprocess.Popen(['pymol', cif_path])
    # Open the image in the default image viewer
    subprocess.Popen(['xdg-open', png_path])  # For Linux, change as needed for Windows or Mac

def retrieve_alphafold_data(event=None, uniprot_id=None, root=None):
    if not uniprot_id:
        messagebox.showerror("Input Error", "Please enter a UniProt accession ID.")
        return

    try:
        data = fetch_alphafold_data(uniprot_id, API_KEY)
        if data:
            root_window = root if root else event.widget.master
            display_data(root_window, data)
            
            # Download and open files
            base_dir = os.path.join(os.getcwd(), "downloaded_files")
            os.makedirs(base_dir, exist_ok=True)
            
            for item in data:
                pdb_url = item.get("pdbUrl")
                cif_url = item.get("cifUrl")
                bcif_url = item.get("bcifUrl")
                png_url = item.get("paeImageUrl")
                
                pdb_path = os.path.join(base_dir, f"{uniprot_id}.pdb")
                cif_path = os.path.join(base_dir, f"{uniprot_id}.cif")
                bcif_path = os.path.join(base_dir, f"{uniprot_id}.bcif")
                png_path = os.path.join(base_dir, f"{uniprot_id}.png")
                
                if pdb_url:
                    download_file(pdb_url, pdb_path)
                if cif_url:
                    download_file(cif_url, cif_path)
                if bcif_url:
                    download_file(bcif_url, bcif_path)
                if png_url:
                    download_file(png_url, png_path)

                # Open the files after downloading
                open_files(pdb_path, cif_path, bcif_path, png_path)
                
        else:
            messagebox.showinfo("No Data", "No data found for the given UniProt accession ID.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("API Error", f"Failed to retrieve data: {e}")

