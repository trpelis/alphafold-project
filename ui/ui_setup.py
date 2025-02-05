from ui.event_handlers import retrieve_alphafold_data, open_hpc_submission_window
import tkinter as tk
from tkinter import ttk, filedialog

def setup_main_window(on_exit):
    root = tk.Tk()
    root.title("Molecular Prediction Tool")
    root.geometry("500x400")
    root.minsize(500, 400)
    root.resizable(True, True)

    # Create input field for UniProt ID
    tk.Label(root, text="UniProt Accession ID:").pack(pady=10)
    entry_uniprot_id = tk.Entry(root, width=30)
    entry_uniprot_id.pack(pady=5)

    # Bind the Enter key to retrieve AlphaFold data
    entry_uniprot_id.bind('<Return>', lambda event: retrieve_alphafold_data(event, entry_uniprot_id.get(), root))

    # Create the three task buttons
    btn_alpha_fold = ttk.Button(root, text="Retrieve AlphaFold Data", command=lambda: retrieve_alphafold_data(None, entry_uniprot_id.get(), root))
    btn_alpha_fold.pack(pady=10, padx=20, fill=tk.X)

    btn_hpc_job = ttk.Button(root, text="Submit HPC Prediction Job", command=open_hpc_submission_window)
    btn_hpc_job.pack(pady=10, padx=20, fill=tk.X)

    def browse_fasta_files():
        fasta_path = filedialog.askopenfilename(
            title="Select FASTA File",
            filetypes=[("FASTA files", "*.fasta"), ("All files", "*.*")]
        )
        if fasta_path:
            print(f"Selected file: {fasta_path}")
            # Here you can add additional logic if you want to do something with the selected FASTA file

    btn_browse_fasta = ttk.Button(root, text="Browse .fasta Files", command=browse_fasta_files)
    btn_browse_fasta.pack(pady=10, padx=20, fill=tk.X)

    root.protocol("WM_DELETE_WINDOW", on_exit)

    return root, entry_uniprot_id

