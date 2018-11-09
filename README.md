These rutines along with associated static calibration files should allow the quick reduction of X-shooter spectra.

Put your science files in the arm/target directory and run the scripts.

This script relies on Python 2.7 and astropy. To setup with conda do:

```
conda create -n py27 python=2.7
```

conda install astropy

You should then be able to run the scripts using:

python NIR.py



See https://github.com/martinsparre/XSHPipelineManager for the original source. All credit for this goes to Martin Sparre. 
