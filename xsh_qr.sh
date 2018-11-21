#!/bin/sh
echo "Running UVB, VIS and NIR in the shell simultaneously"

cd UVB
python UVB.py &> UVB.log &
cd ..
cd VIS
python VIS.py &> VIS.log &
cd ..
cd NIR
python NIR.py &> NIR.log &
cd ..


