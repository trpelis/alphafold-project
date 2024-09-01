import pytest
from pbs_scripts import generate_cpu_pbs_script

def test_generate_cpu_pbs_script():
    job_name = "test_job"
    fasta_path = "/path/to/test.fasta"
    data_dir = "/path/to/data"
    output_dir = "/path/to/output"
    max_template_date = "2025-08-21"

    pbs_script = generate_cpu_pbs_script(job_name, fasta_path, data_dir, output_dir, max_template_date)

    print(pbs_script)  # Print the script to debug
    assert "#PBS -N test_job" in pbs_script
    assert "--fasta_paths=/path/to/test.fasta" in pbs_script
    assert "--data_dir=/path/to/data" in pbs_script

