import unittest
from unittest.mock import patch, MagicMock
from hpc_utils import HPCConnection
from ui.event_handlers import submit_job


class TestJobSubmission(unittest.TestCase):

    @patch('ui.event_handlers.filedialog.askopenfilename')
    @patch('ui.event_handlers.HPCConnection.upload_file')
    @patch('ui.event_handlers.HPCConnection.submit_job')
    @patch('ui.event_handlers.HPCConnection.monitor_job')
    @patch('ui.event_handlers.HPCConnection.download_file')
    @patch('tkinter.Tk', return_value=MagicMock())  # Mock Tk to avoid GUI dependencies
    def test_submit_cpu_job(self, mock_tk, mock_download, mock_monitor, mock_submit, mock_upload, mock_askopenfilename):
        # Setup the mock return values
        mock_askopenfilename.return_value = "/local/path/to/test.fasta"
        mock_submit.return_value = "12345.job"
        mock_monitor.return_value = True

        # Call the function to be tested
        submit_job("/local/path/to/test.fasta")

        # Assertions to check that each mocked method was called correctly
        mock_upload.assert_called_once_with("/local/path/to/test.fasta", "/lustre/home/trajevsk/test.fasta")
        mock_submit.assert_called_once_with("/lustre/home/trajevsk/alphapulldown.pbs", "/local/path/to/test.fasta")
        mock_monitor.assert_called_once_with("12345.job")
        mock_download.assert_called_once_with(
            "/lustre/home/trajevsk/output/test.fasta.result", 
            "/home/trpimraj/zavrsni/alphafold-project/tests/test.fasta.result"
        )


if __name__ == '__main__':
    unittest.main()

