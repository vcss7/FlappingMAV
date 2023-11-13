#!/bin/bash
# This file is called by the objfunc.f95 file.

# Read parameters from a file, update the UVLM simulation file, run UVLM, and
# save the results in a file.

# Read files
declare -a files
declare -a param

# get parameters from file
param=(`awk '{print $1}' < param.txt`)


# set parameters for UVLM simulation
AMP_X=${param[0]}
AMP_Y=${param[1]}
AMP_ROT=${param[2]}
PHI_X=${param[3]}
PHI_Y=${param[4]}


# make a new file for each simulation run
cp ../ring_uvlm_solver_static_original.py ring_uvlm_solver_static.py
# update the UVLM simulation file
sed -i -e "s/AMP_X = 0.0/AMP_X = $AMP_X/g" ring_uvlm_solver_static.py
sed -i -e "s/AMP_Y = 0.0/AMP_Y = $AMP_Y/g" ring_uvlm_solver_static.py
sed -i -e "s/AMP_ROT = 0.0/AMP_ROT = $AMP_ROT/g" ring_uvlm_solver_static.py
sed -i -e "s/PHI_X = 0.0/PHI_X = $PHI_X/g" ring_uvlm_solver_static.py
sed -i -e "s/PHI_Y = 0.0/PHI_Y = $PHI_Y/g" ring_uvlm_solver_static.py


# run UVLM and save lift coeffecient (objfunc value) result in a file
python3 ring_uvlm_solver_static.py | grep CL | awk '{print $2}' > CL.dat


# prepare results file for objfunc.f95
# create a new file that has the parameters used in a row
awk '{ printf "%s ", $0 } END { printf "\n" }' param.txt > param.dat


# save results in a file
# formatted as follows:
# param1 param2 param3 ... paramN objfunc
paste param.dat CL.dat > results.dat

