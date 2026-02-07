<div align="center">
  <h1>AlphaFold HPC Submission &amp; Visualization Platform</h1>
  <p>
    A molecular prediction platform that lets users submit protein sequences (FASTA) to an HPC environment,
    run AlphaPulldown jobs (CPU or GPU), and visualize results using PyMOL and external database integrations.
  </p>
</div>

<hr>

<h2>Overview</h2>
<p>
  The AlphaFold Project is a molecular prediction application that allows users to submit protein sequences in FASTA format
  to an HPC (High-Performance Computing) environment for processing using AlphaPulldown. The results are retrieved and
  visualized using integrated tools like PyMOL.
</p>
<p>
  The application supports both CPU and GPU job submissions, providing flexibility in how computational resources are utilized.
  It integrates with external databases via API calls, allowing users to retrieve and display molecular structures and related
  data directly within the app.
</p>

<hr>

<h2>Architecture</h2>

<h3>High Level System Design</h3>
<div align="center">
  <img
    src="https://github.com/user-attachments/assets/94526cb3-ad45-44bb-a595-2d6724f2b3a6"
    alt="System architecture overview"
    width="820"
  >
  <br>
  <sub><b>Figure 1 — System architecture overview</b></sub>
</div>

<br>
<h3>Component View</h3>

<div align="center">
  <img
    src="https://github.com/user-attachments/assets/e1b68618-a422-42c8-8506-3b649b4ecfd6"
    alt="Component view"
    width="48%"
  >
  <img
    src="https://github.com/user-attachments/assets/5f5ab151-a5f1-4ff8-8b83-637d9e1c6734"
    alt="Component view (detail)"
    width="48%"
  >
  <br>
  <sub><b>Figure 2 — Core service components</b></sub>
</div>

<br>

<div align="center">
  <img
    src="https://github.com/user-attachments/assets/e048beb5-d08a-4283-813e-b2ce9264b05f"
    alt="HPC workflow"
    width="48%"
  >
  <img
    src="https://github.com/user-attachments/assets/befd1616-47d5-4d6a-8d1c-7f8021e6f59d"
    alt="Job lifecycle"
    width="48%"
  >
  <br>
  <sub><b>Figure 3 — HPC workflow and job lifecycle</b></sub>
</div>

<hr>

<h2>User Interface</h2>

<h3>Graphical Interface</h3>
<div align="center">
  <img
    src="https://github.com/user-attachments/assets/0d9249ab-0b01-46f8-b75d-7ef2adb99016"
    alt="GUI screenshot 1"
    width="78%"
  >
  <br><br>
  <img
    src="https://github.com/user-attachments/assets/5ed49a5f-688b-4bd9-89a0-0bf38072ea9a"
    alt="GUI screenshot 2"
    width="78%"
  >
  <br><br>
  <img
    src="https://github.com/user-attachments/assets/400f5eb8-03a7-4bf9-9d91-af360dfd07dc"
    alt="GUI screenshot 3"
    width="78%"
  >
  <br>
  <sub><b>Figure 4 — GUI workflow and visualization</b></sub>
</div>

<br>

<h3>CLI Interaction</h3>
<div align="center">
  <img
    src="https://github.com/user-attachments/assets/7b5cc96d-22e6-45b5-ab0d-439a274ea508"
    alt="CLI output 1"
    width="92%"
  >
  <br><br>
  <img
    src="https://github.com/user-attachments/assets/af404576-08cf-4b37-81c9-75436beb783b"
    alt="CLI output 2"
    width="92%"
  >
  <br>
  <sub><b>Figure 5 — Command-line execution and output</b></sub>
</div>

<hr>

<h2>Key Features</h2>
<ul>
  <li>FASTA sequence submission</li>
  <li>CPU and GPU job scheduling</li>
  <li>AlphaPulldown integration</li>
  <li>HPC cluster execution</li>
  <li>Automated result retrieval</li>
  <li>PyMOL visualization</li>
  <li>External biological database API integration</li>
  <li>GUI and CLI interfaces</li>
</ul>

<hr>

<h2>Typical Workflow</h2>
<ol>
  <li>Provide protein FASTA sequence</li>
  <li>Select CPU or GPU execution</li>
  <li>Submit job to HPC cluster</li>
  <li>Monitor execution status</li>
  <li>Retrieve predicted structure</li>
  <li>Visualize molecule interactively</li>
</ol>

<hr>

<h2>Use Cases</h2>
<ul>
  <li>Bioinformatics research</li>
  <li>Protein structure validation</li>
  <li>Drug discovery pipelines</li>
  <li>Educational molecular visualization</li>
  <li>HPC workflow automation demonstrations</li>
</ul>
