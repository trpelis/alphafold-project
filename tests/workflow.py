from tkinter import Tk
from unittest.mock import Mock, patch
from ui.event_handlers import retrieve_alphafold_data
import pytest

@patch('ui.event_handlers.fetch_alphafold_data')
@patch('ui.event_handlers.download_file')
@patch('ui.event_handlers.open_files')
def test_full_workflow(mock_fetch, mock_open_files, mock_download):
    mock_data = [{
        'entryId': 'test_entry',
        'gene': 'TestGene',
        'pdbUrl': 'http://example.com/test.pdb',
        'cifUrl': 'http://example.com/test.cif',
        'bcifUrl': 'http://example.com/test.bcif',
        'paeImageUrl': 'http://example.com/test.png'
    }]
    mock_fetch.return_value = mock_data

    # Create a real Tk root window
    root = Tk()
    root.withdraw()  # Hide the root window

    try:
        result = retrieve_alphafold_data(uniprot_id="P12345", root=root)
        assert result is not None
    finally:
        root.destroy()

