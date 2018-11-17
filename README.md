These rutines along with associated static calibration files should allow the quick reduction of X-shooter spectra.

This script relies on Python 2.7 and astropy. To setup with conda do:

```
conda create -n py27 python=2.7
```

```
conda install astropy
```

Put the downloaded science images to the corresponding folders: XSHPipelineManager/ARM/target. Important, do not change the name of the folder (target). The files have to be unzipped.

You should then be able to run the scripts using:

```
python NIR.py
```

By default the pipeline runs in nodding mode, i.e. you need to provide at least two files (one nodding cycle) per arm. If you want to 
run the pipeline in staring mode, comment the following line in the ARM.py file:

```

```

In the case of staring reduction the pipeline checks the DIT in the NIR arm and chooses the correct masterdark.

The pipeline checks whether observation is done in the K-blocking mode or not. 

Wavelengths are in air. No extinction correction.

See https://github.com/martinsparre/XSHPipelineManager for the original source. All credit for this goes to Martin Sparre. 
