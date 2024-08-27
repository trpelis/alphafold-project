import time
from fabric import Connection

hpc_host = 'trajevsk@login-cpu.hpc.srce.hr'
remote_working_directory = '/lustre/home/trajevsk/'

class HPCConnection:
    def __init__(self):
        self.conn = Connection(hpc_host)

    def upload_file(self, local_path, remote_path):
        """Upload a file from local_path to remote_path on the HPC server."""
        try:
            with self.conn.sftp() as sftp:
                sftp.put(local_path, remote_path)
                print(f"Uploaded {local_path} to {remote_path}")
        except Exception as e:
            print(f"Error uploading file: {e}")

    def run_command(self, command):
        """Run a command on the HPC server."""
        try:
            result = self.conn.run(command, hide=True)
            return result.stdout.strip()
        except Exception as e:
            print(f"Error running command: {e}")
            return None

    def submit_job(self):
        """Submit the job on the HPC using the pre-configured PBS script."""
        try:
            command = f"cd {remote_working_directory} && qsub alphapulldown.pbs"
            job_id = self.run_command(command)
            print(f"Job submitted with ID: {job_id}")
            return job_id
        except Exception as e:
            print(f"Error submitting job: {e}")
            return None

    def monitor_job(self, job_id):
        """Monitor the HPC job until it completes."""
        job_completed = False
        while not job_completed:
            try:
                job_state = self.run_command(f"qstat -f {job_id} | grep job_state")
                if job_state:
                    job_state = job_state.split('=')[-1].strip()
                    if job_state in ['C', 'F']:
                        job_completed = True
                else:
                    print(f"Job {job_id} has finished or not found.")
                    job_completed = True
            except Exception as e:
                print(f"Error monitoring job: {e}")
                break
            if not job_completed:
                time.sleep(60)
        print(f"Job {job_id} completed.")
        return job_completed

    def close(self):
        """Close the HPC connection."""
        self.conn.close()
        print("Connection closed")

