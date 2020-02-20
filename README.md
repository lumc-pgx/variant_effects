# VEP module for the Pharmacogenomics Pipeline

**This module leverages ensembl VEP to predict the impact of genomic variants.**  

The variant effects module performs the following operations:
- Prediction of variant effects using ensembl VEP
- Filtering and collation of effect predictions

## Requirements
- [Conda/Miniconda](https://conda.io/miniconda.html)  

## Installation
- Clone the repository
  - `git clone https://github.com/lumc-pgx/variant_effects.git`

- Change to the variant_calling directory
  - `cd variant_effect`

- Create a conda environment for running the pipeline
  - `conda env create -n variant_effects -f environment.yaml`

- In order to use the pipeline on the cluster, update your .profile to use the drmaa library:
  - `echo "export DRMAA_LIBRARY_PATH=libdrmaa.so.1.0" >> ~/.profile`
  - `source ~/.profile`

## Configuration
The pipeline configuration settings are specified in [config.yaml](config.yaml).  
Edit the configfile with run-specific paths and settings.  

## Execution
- Activate the conda environment
  - `source activate variant_effects`
- For parallel execution on the cluster
  - `pipe-runner --configfile config.yaml`
- To specify that the pipeline should write output to a location other than the default:
  - `pipe-runner --configfile config.yaml --directory path/to/output/directory`
