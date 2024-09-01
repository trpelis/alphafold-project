from unittest.mock import patch, Mock
import pytest
from hpc_utils import HPCConnection
from ui.event_handlers import submit_job

@patch.object(HPCConnection, 'upload_file')
@patch.object(HPCConnection, 'submit_job')
@patch.object(HPCConnection, 'monitor_job')
@patch.object(HPCConnection, 'download_file')
def test_submit_cpu_job(mock_download, mock_monitor, mock_submit, mock_upload):
    mock_submit.return_value = "12345.job"
    mock_monitor.return_value = True

    fasta_path = "/home/trpimraj/zavrsni/alphafold-project/examp.fasta"  # Adjust to match actual path
    submit_job(fasta_path)

    mock_upload.assert_called_once_with(fasta_path, '/lustre/home/trajevsk/examp.fasta')


