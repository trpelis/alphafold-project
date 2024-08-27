import os
import time
import requests
import tkinter as tk
from tkinter import messagebox, filedialog
from ui.data_display import display_data
from config.config import API_KEY
from api.fetcher import fetch_alphafold_data
from hpc_utils import HPCConnection


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

def open_hpc_submission_window():
    submission_window = tk.Toplevel()
    submission_window.title("Submit HPC Prediction Job")
    submission_window.geometry("300x200")

    cpu_button = tk.Button(submission_window, text="CPU Prediction", command=lambda: open_cpu_submission_window(submission_window))
    cpu_button.pack(pady=20)

    gpu_button = tk.Button(submission_window, text="GPU Prediction", command=lambda: open_gpu_submission_window(submission_window))
    gpu_button.pack(pady=20)

def open_cpu_submission_window(parent_window):
    parent_window.destroy()

    cpu_window = tk.Toplevel()
    cpu_window.title("CPU Prediction Job")
    cpu_window.geometry("400x400")

    tk.Label(cpu_window, text="Job Name:").pack(pady=5)
    job_name_entry = tk.Entry(cpu_window, width=40)
    job_name_entry.pack(pady=5)

    tk.Label(cpu_window, text="FASTA File Path:").pack(pady=5)
    fasta_path_entry = tk.Entry(cpu_window, width=40)
    fasta_path_entry.pack(pady=5)

    # Button to open file dialog for selecting the FASTA file
    def browse_fasta_file():
        fasta_path = filedialog.askopenfilename(
            title="Select FASTA File",
            filetypes=(("FASTA files", "*.fasta"), ("All files", "*.*"))
        )
        fasta_path_entry.delete(0, tk.END)
        fasta_path_entry.insert(0, fasta_path)

    browse_button = tk.Button(cpu_window, text="Browse", command=browse_fasta_file)
    browse_button.pack(pady=5)

    submit_btn = tk.Button(cpu_window, text="Submit CPU Job", command=lambda: submit_cpu_job(fasta_path_entry.get()))
    submit_btn.pack(pady=20)

def submit_cpu_job(fasta_path):
    hpc = HPCConnection()

    # Define paths
    remote_fasta_path = f"/lustre/home/trajevsk/{os.path.basename(fasta_path)}"

    # Upload the FASTA file to the HPC
    hpc.upload_file(fasta_path, remote_fasta_path)

    # Submit the pre-configured PBS script as a job
    job_id = hpc.submit_job()

    if job_id:
        # Monitor the job
        hpc.monitor_job(job_id)

    # Close the connection
    hpc.close()

def notify_user(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Notification", message)
    root.destroy()

