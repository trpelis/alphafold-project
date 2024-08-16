import time
from fabric import Connection
from invoke import UnexpectedExit

hpc_host = 'trajevsk@login-cpu.hpc.srce.hr'
base_remote_working_directory = '/lustre/home/trajevsk/alphafold'

class HPCConnection:
    def __init__(self):
        self.conn = Connection(hpc_host)

    def upload_script_content(self, script_content, remote_path):
        with self.conn.sftp() as sftp:
            with sftp.file(remote_path, 'w') as f:
                f.write(script_content)

    def run_command(self, command):
        result = self.conn.run(command, hide=True)
        return result.stdout.strip()

    def download_file(self, remote_path, local_path):
        # Ensure that the SFTP connection is active before downloading
        with self.conn.sftp() as sftp:
            sftp.get(remote_path, local_path)

    def close(self):
        self.conn.close()

    def submit_job(self, pbs_script, job_name):
        remote_pbs_path = f"{base_remote_working_directory}/{job_name}.pbs"
        self.upload_script_content(pbs_script, remote_pbs_path)
        job_id = self.run_command(f"qsub {remote_pbs_path}")
        return job_id

    def monitor_job(self, job_id):
        job_completed = False
        while not job_completed:
            try:
                job_state = self.run_command(f"qstat -f {job_id} | grep job_state")
                job_state = job_state.split('=')[-1].strip()
                if job_state in ['C', 'F']:
                    job_completed = True
            except UnexpectedExit as e:
                if "Job has finished" in str(e):
                    job_completed = True
                else:
                    raise e
            if not job_completed:
                time.sleep(60)
        return job_completed

