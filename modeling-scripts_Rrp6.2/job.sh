
#!/bin/bash
#
#$ -S /bin/bash
#$ -l netapp=1G,scratch=1G
#$ -cwd
#$ -o /netapp/sali/pellarin/exosome/modeling-scripts_Rrp6.2/
#$ -e /netapp/sali/pellarin/exosome/modeling-scripts_Rrp6.2/
#$ -l arch=linux-x64
#$ -l mem_free=2G
#$ -pe ompi 64
#$ -q lab.q
#$ -R yes
#$ -l netappsali=2G                  
#$ -l scrapp=2G
#$ -V
#$ -l h_rt=300:00:0.
#$ -t 1
#$ -N exo.R.2

# 1 job name           exo.R.2
# 1 template directory modeling-scripts_Rrp6
# 1 final directory    modeling-scripts_Rrp6.2
# 1 script name        exosome.modeling.py
#########################################

  
# load MPI modules
module load openmpi-1.6-nodlopen
module load sali-libraries
# IMP stuff

export IMP=/netapp/sali/pellarin/imp-160614/imp-fast-mpich/setup_environment.sh

# write hostname and starting time 
hostname
date

# run the job
mpirun -np $NSLOTS $IMP python exosome.modeling.py

# done
date
