import tkinter as tk

def display_data(root, data):
    new_window = tk.Toplevel(root)
    new_window.title("AlphaFold Data")
    new_window.geometry("600x700")
    new_window.minsize(600, 700)

    text_widget = tk.Text(new_window, wrap=tk.WORD)
    text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    for item in data:
        text_widget.insert(tk.END, f"Entry ID: {item.get('entryId', 'N/A')}\n")
        text_widget.insert(tk.END, f"Gene: {item.get('gene', 'N/A')}\n")
        text_widget.insert(tk.END, f"Sequence Checksum: {item.get('sequenceChecksum', 'N/A')}\n")
        text_widget.insert(tk.END, f"Sequence Version Date: {item.get('sequenceVersionDate', 'N/A')}\n")
        text_widget.insert(tk.END, f"UniProt Accession: {item.get('uniprotAccession', 'N/A')}\n")
        text_widget.insert(tk.END, f"UniProt ID: {item.get('uniprotId', 'N/A')}\n")
        text_widget.insert(tk.END, f"UniProt Description: {item.get('uniprotDescription', 'N/A')}\n")
        text_widget.insert(tk.END, f"Tax ID: {item.get('taxId', 'N/A')}\n")
        text_widget.insert(tk.END, f"Organism: {item.get('organismScientificName', 'N/A')}\n")
        text_widget.insert(tk.END, f"UniProt Start: {item.get('uniprotStart', 'N/A')}\n")
        text_widget.insert(tk.END, f"UniProt End: {item.get('uniprotEnd', 'N/A')}\n")
        text_widget.insert(tk.END, f"Sequence: {item.get('uniprotSequence', 'N/A')}\n")
        text_widget.insert(tk.END, f"Model Created Date: {item.get('modelCreatedDate', 'N/A')}\n")
        text_widget.insert(tk.END, f"Latest Version: {item.get('latestVersion', 'N/A')}\n")
        text_widget.insert(tk.END, f"All Versions: {', '.join(map(str, item.get('allVersions', [])))}\n")
        text_widget.insert(tk.END, f"Is Reviewed: {item.get('isReviewed', 'N/A')}\n")
        text_widget.insert(tk.END, f"Is Reference Proteome: {item.get('isReferenceProteome', 'N/A')}\n")
        text_widget.insert(tk.END, f"CIF URL: {item.get('cifUrl', 'N/A')}\n")
        text_widget.insert(tk.END, f"BCIF URL: {item.get('bcifUrl', 'N/A')}\n")
        text_widget.insert(tk.END, f"PDB URL: {item.get('pdbUrl', 'N/A')}\n")
        text_widget.insert(tk.END, f"PAE Image URL: {item.get('paeImageUrl', 'N/A')}\n")
        text_widget.insert(tk.END, f"PAE Doc URL: {item.get('paeDocUrl', 'N/A')}\n")
        text_widget.insert(tk.END, f"AM Annotations URL: {item.get('amAnnotationsUrl', 'N/A')}\n")
        text_widget.insert(tk.END, f"AM Annotations Hg19 URL: {item.get('amAnnotationsHg19Url', 'N/A')}\n")
        text_widget.insert(tk.END, f"AM Annotations Hg38 URL: {item.get('amAnnotationsHg38Url', 'N/A')}\n")
        text_widget.insert(tk.END, "-" * 60 + "\n\n")

    text_widget.config(state=tk.DISABLED)

