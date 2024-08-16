def generate_cpu_pbs_script(job_name, fasta_path, data_dir, output_dir, max_template_date):
    pbs_script = f"""
#!/bin/bash
#PBS -N {job_name}
#PBS -q cpu
#PBS -l select=1:ncpus=8:mem=40GB


cd $PBS_O_WORKDIR

# Activate AlphaPulldown environment
module load scientific/alphapulldown/0.30.7


# Run the create_individual_features.py script
create_individual_features.py \\
  --fasta_paths={fasta_path} \\
  --data_dir={data_dir} \\
  --output_dir={output_dir} \\
  --max_template_date={max_template_date}
    """
    return pbs_script


def generate_gpu_pbs_script(job_name, output_dir, protein_lists):
    pbs_script = f"""
#!/bin/bash
#PBS -N {job_name}
#PBS -q gpu
#PBS -l select=1:ncpus=8:mem=40GB:ngpus=1

cd $PBS_O_WORKDIR

module load scientific/alphapulldown/0.30.7

alphapulldown.sh run_multimer_jobs.py --mode=pulldown --num_cycle=3 --num_predictions_per_model=1 --output_path={output_dir} --data_dir=$ALPHADB --protein_lists={protein_lists} --monomer_objects_dir=out --job_index=1
    """
    return pbs_script
