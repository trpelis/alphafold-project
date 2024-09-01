from tkinter import Tk
from unittest.mock import Mock, patch
from ui.event_handlers import retrieve_alphafold_data
import pytest

@patch('ui.event_handlers.fetch_alphafold_data')
@patch('ui.event_handlers.download_file')
@patch('ui.event_handlers.open_files')
@patch('tkinter.Toplevel')  # Mock Toplevel as well if used in your code
@patch('tkinter.Tk', spec=Tk)  # Mock Tk, but ensure it behaves like a Tk instance
def test_full_workflow(mock_tk, mock_toplevel, mock_fetch, mock_open_files, mock_download):
    mock_data = [{
        'entryId': 'test_entry',
        'gene': 'TestGene',
        'pdbUrl': 'http://example.com/test.pdb',
        'cifUrl': 'http://example.com/test.cif',
        'bcifUrl': 'http://example.com/test.bcif',
        'paeImageUrl': 'http://example.com/test.png'
    }]
    mock_fetch.return_value = mock_data

    # Ensure the mock Tk window behaves more like a real Tk instance
    mock_tk_instance = mock_tk.return_value
    mock_tk_instance._last_child_ids = {}

    # Call the function you want to test
    result = retrieve_alphafold_data(uniprot_id="P12345", root=mock_tk_instance)
    
    # Validate the result
    assert result is not None
