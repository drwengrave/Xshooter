These rutines along with associated static calibration files should allow the quick reduction of X-shooter spectra.

This script relies on Python 2.7 and astropy. To setup with conda do:

```
conda create -n py27 python=2.7
```

```
conda install astropy
```

You should then be able to run the scripts using:

```
python ARM.py
```

where ARM=UVB, VIS or NIR.

The pipeline is made to be robust and there is not a lot of flexibility allowed. A few things can be changed in the ARM.py scripts though (clearly indicated in the scripts).

You can change the folder name in which you have the data to be reduced. The default is: XSHPipelineManager/ARM/target. We recommend the same folder structure. The fits images have to be unzipped.

By default the pipeline runs in nodding mode, i.e. you need to provide at least two files (one nodding cycle) per arm. If you want to 
run the pipeline in staring mode, comment the nodding- and uncomment the staring-mode lines in the ARM.py scripts.

In the case of staring reduction the pipeline checks the DIT in the NIR arm and chooses the correct masterdark.

The pipeline checks whether observation is done in the K-blocking mode or not. 

Wavelengths are in air. No extinction correction is applied to the final products.

See https://github.com/martinsparre/XSHPipelineManager for the original source. All credit for this goes to Martin Sparre. 
