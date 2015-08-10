##Modeling exosome complexes from cross-link MS data:

This repository contains the modeling scripts, the ensemble of models, and the results of the analysis for the modeling of the S.cerevisiae exosome complex (named exo10, comprising of Rrp40, Rrp4, Csl4, Rrp45, Rrp46, Rrp42, Rrp43, Mtr3, Ski6 and Rrp44), in presence of Ski7 (exo10+Ski7 below) or Rrp6 (exo10+Rrp6 below) proteins. The modeling is performed based on cross-link Mass-Spectrometry data, crystallographic structures, and homology models. 

The complete description of the project and the modeling procedure can be found in:

A strategy for dissecting the architectures of endogenous macromolecular assemblies

Yi Shi, Riccardo Pellarin, Peter C. Fridy, Javier Fernandez-Martinez, Mary K. Thompson, Yinyin Li, Qing Jun Wang, Andrej Sali, Michael P. Rout, and Brian T. Chait.

##Displaying the models
To display the models and the localization densities using UCSF chimera access `./Rrp6.analysis/kmeans_weight_500_2/cluster.1/` or `./Ski7.analysis/kmeans_weight_500_2/cluster.1/` and run `chimera chimera.session.py`

##Compatibility:

The scripts are running safely with `IMP.pmi` git hash  `61b7834aa9fac2960641415b4c90651e7015a048`, `IMP` git hash `38754464b774041e315fbae1820183f4ccc29106`.


## Running the modeling script:

For more details on how to install imp, run the modeling scripts and analyse the results using IMP and IMP.pmi see the tutorial 

http://integrativemodeling.org/systems/tutorial

In brief, to use the Replica Exchange, IMP must be compiled using an openmpi c++ compiler. We suggest to compile openmpi with the `--disable-dlopen` flag.

See IMP building instructions in: https://integrativemodeling.org/nightly/doc/html/installation.html

Tu run the modeling script, access: `sampling/modeling` and then run with 64 threads (64 replicas):

``mpirun -np 64 imp_build_directory/setup_environment.sh python modeling.py``


## Content of the directories:


`modeling-scripts_Rrp6.1`     modeling scripts and output modeling data for exo10+Rrp6 complex (first calculation)

`modeling-scripts_Rrp6.2`     modeling scripts and output modeling data for exo10+Rrp6 complex (second calculation)

`modeling-scripts_Ski7.1`     modeling scripts and output modeling data for exo10+Ski7 complex (first calculation)

`modeling-scripts_Ski7.2`     modeling scripts and output modeling data for exo10+Ski7 complex (second calculation)

`README.md` this readme file

`Rrp6.analysis`     analysis for exo10+Rrp6 complex

`Ski7.analysis`     analysis for exo10+Ski7 complex

`data`		  cross-linking data, fasta files, pdbs needed for the calculation

`metadata`   files needed for the repository


#Content of the `modeling-scripts*` directories:

`exosome.modeling.py`   		modeling script (see above)

`job.sh` 		      		computer-cluster submission script (for UCSF QB3 cluster)

`output`		      		all output data

`output/pdbs`           		best scoring 500 pdb files

`output/rmfs`           		rmf files for each replica

`output/stat.*.out`     		stat files containing modeling data (the index is the index of replica). To be read 
using the python program `IMP_source/modules/pmi/pyext/src/process_output.py`

`output/stat_replica.*.out`     	stat files containing replica exchange data. To be read using `IMP_source/modules/pmi/pyext/src/process_output.py`


#Content of the `*.analysis` directories:

`clustering.py`: clustering script

`kmeans_weight_500_2`: the set of 500 best scoring models collected in two clusters

`precision_rmsf.py`: calculate the precision of clusters, their mutual distance and the RMSF

`XL_table.py`: calculate the contact map and the cross-link map

`cluster.0`: data for cluster 1

`cluster.1`: data for cluster 2

`precision.0.0.out`,`precision.0.1.out`,... : files containing the precision of a cluster (i.e., the files with the same indexes, `precision.i.i.out`, e.g., `precision.0.0.out`) and the files containing the distance between the clusters (i.e., files with different indexes, `precision.i.j.out`).

#Content of the `*.analysis/cluster.*` directories

`0.pdb`,`1.pdb`,`2.pdb`....: the pdb files of the solutions

`0.rmf3`,`1.rmf3`,`2.rmf3`,...: the rmf files of the solution (can be opened with UCSF Chimera)

`rmsf.Ski7.dat`,`rmsf.Rrp6.dat`,...: text file of the RMSF analysis

`rmsf.Ski7.pdf`,`rmsf.Rrp6.pdf`,...: pdf file of the RMSF analysis

`chimera_session.py`: chimera session file to display the localization densities

`stat.out`: stat file containing all relevant information on the score, etc.

`XL_table_tail.pdf`: pdf file of the cross-link map for the complex


