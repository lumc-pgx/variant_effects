# VEP module for the Pharmacogenomics Pipeline

**This module leverages ensembl VEP to predict the impact of genomic variants.**  

The variant effects module performs the following operations:
- Prediction of variant effects using ensembl VEP
- Filtering and collation of effect predictions

```plantuml
digraph snakemake_dag {
	graph [bb="0,0,76,180",
		bgcolor=white,
		margin=0
	];
	node [fontname=sans,
		fontsize=10,
		label="\N",
		penwidth=2,
		shape=box,
		style=rounded
	];
	edge [color=grey,
		penwidth=2
	];
	0	 [color="0.00 0.6 0.85",
		height=0.5,
		label=link_source,
		pos="38,162",
		width=0.97222];
	2	 [color="0.44 0.6 0.85",
		height=0.5,
		label=vep_process,
		pos="38,90",
		width=1.0625];
	0 -> 2	 [pos="e,38,108.1 38,143.7 38,135.98 38,126.71 38,118.11"];
	1	 [color="0.22 0.6 0.85",
		height=0.5,
		label=all,
		pos="38,18",
		width=0.75];
	2 -> 1	 [pos="e,38,36.104 38,71.697 38,63.983 38,54.712 38,46.112"];
}
```

## Requirements
- [Conda/Miniconda](https://conda.io/miniconda.html)  

## Installation
- Clone the repository
  - `git clone https://git.lumc.nl/PharmacogenomicsPipe/variant_effects.git`

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
