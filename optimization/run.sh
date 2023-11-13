#!/bin/bash

export LD_LIBRARY_PATH=/usr/lib64/openmpi/lib/

# Compile
mpif90 -g -O -o pmain shared_modules.f95 pVTdirect.f95 sample_pmain.f95

cd ./parallel
rm -f CL.dat
rm -rf test_*
mpirun -np 8 ../pmain

exit
