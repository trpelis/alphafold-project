from tkinter import Tk
from unittest.mock import Mock, patch
from ui.event_handlers import retrieve_alphafold_data
import pytest

@patch('ui.event_handlers.fetch_alphafold_data')
@patch('ui.event_handlers.download_file')
@patch('ui.event_handlers.open_files')
@patch('tkinter.Tk')  # Mock the entire Tk class
@patch('tkinter.Toplevel')  # Mock the Toplevel class if it's used
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

    # Create a mock Tk root window
    mock_tk.return_value = Mock()

    result = retrieve_alphafold_data(uniprot_id="P12345", root=mock_tk.return_value)
    assert result is not None

