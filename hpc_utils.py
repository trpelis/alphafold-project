import time
from fabric import Connection

hpc_host = 'trajevsk@login-cpu.hpc.srce.hr'
base_remote_working_directory = '/lustre/home/trajevsk/alphafold'

class HPCConnection:
    def __init__(self):
        self.conn = Connection(hpc_host)

    def upload_file(self, local_path, remote_path):
        try:
            self.conn.put(local_path, remote_path)
            print(f"Uploaded {local_path} to {remote_path}")
        except Exception as e:
            print(f"Failed to upload {local_path}: {e}")

    def download_file(self, remote_path, local_path):
        try:
            self.conn.get(remote_path, local=local_path)
            print(f"Downloaded {remote_path} to {local_path}")
        except Exception as e:
            print(f"Failed to download {remote_path}: {e}")

    def submit_job(self, remote_pbs_path, job_type):
        try:
            job_id = self.conn.run(f"qsub {remote_pbs_path}", hide=True).stdout.strip()
            print(f"Job submitted with ID: {job_id}")
            return job_id
        except Exception as e:
            print(f"Failed to submit job: {e}")
            return None

    def monitor_job(self, job_id):
        job_completed = False
        while not job_completed:
            try:
                result = self.conn.run(f"qstat -f {job_id} | grep job_state", hide=True).stdout.strip()
                if result:
                    job_state = result.split('=')[-1].strip()
                    if job_state in ['C', 'F']:
                        job_completed = True
                else:
                    print(f"Job {job_id} has finished or not found.")
                    job_completed = True
            except Exception as e:
                print(f"Error checking job status: {e}")
                job_completed = True

            if not job_completed:
                time.sleep(60)
        print(f"Job {job_id} completed.")

    def close(self):
        self.conn.close()
