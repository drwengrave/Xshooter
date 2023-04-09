import numpy as np
import os.path
script_path = os.path.abspath(os.getcwd())
from matplotlib import pyplot as plt

def avg(flux, error, mask=None, axis=2, weight=False, weight_map=None):

    """Calculate the weighted average with errors
    ----------
    flux : array-like
        Values to take average of
    error : array-like
        Errors associated with values, assumed to be standard deviations.
    mask : array-like
        Array of bools, where true means a masked value.
    axis : int, default 0
        axis argument passed to numpy

    Returns
    -------
    average, error : tuple

    Notes
    -----
    """
    try:
        if not mask:
            mask = np.zeros_like(flux).astype("bool")
    except:
        pass
        # print("All values are masked... Returning nan")
        # if np.sum(mask.astype("int")) == 0:
        #     return np.nan, np.nan, np.nan


    # Normalize to avoid numerical issues in flux-calibrated data
    norm = abs(np.ma.median(flux[flux > 0]))
    if norm == np.nan or norm == np.inf or norm == 0:
        print("Nomalization factor in avg has got a bad value. It's "+str(norm)+" ... Replacing with 1")

    flux_func = flux.copy() / norm
    error_func = error.copy() / norm

    # Calculate average based on supplied weight map
    if weight_map is not None:

        # Remove non-contributing pixels
        flux_func[mask] = 0
        error_func[mask] = 0
        # https://physics.stackexchange.com/questions/15197/how-do-you-find-the-uncertainty-of-a-weighted-average?newreg=4e2b8a1d87f04c01a82940d234a07fc5
        average = np.ma.sum(flux_func * weight_map, axis=axis) / np.ma.sum(weight_map, axis=axis)
        variance = np.ma.sum(error_func**2 * weight_map**2, axis=axis) / np.ma.sum(weight_map, axis=axis)**2



    # Inverse variance weighted average
    elif weight:
        ma_flux_func = np.ma.array(flux_func, mask=mask)
        ma_error_func = np.ma.array(error_func, mask=mask)
        w = 1.0 / (ma_error_func ** 2.0)
        average = np.ma.sum(ma_flux_func * w, axis=axis) / np.ma.sum(w, axis=axis)
        variance = 1. / np.ma.sum(w, axis=axis)
        if not isinstance(average, float):
            # average[average.mask] = np.nan
            average = average.data
            # variance[variance.mask] = np.nan
            variance = variance.data

    # Normal average
    elif not weight:
        # Number of pixels in the mean
        n = np.ma.sum(np.array(mask).astype(bool), axis=axis)
        # Remove non-contributing pixels
        flux_func[mask.astype(bool)] = 0
        error_func[mask.astype(bool)] = 0
        # mean
        average = (1 / n) * np.ma.sum(flux_func, axis=axis)
        # probagate errors
        variance = (1 / n**2) * np.ma.sum(error_func ** 2.0, axis=axis)

    mask = (np.ma.sum((mask).astype(bool), axis=axis) == 0).astype(bool)
    return (average * norm, np.sqrt(variance)*norm)


def bin_spectrum(wl, flux, error, binh, weight=False):

    """Bin low S/N 1D data from xshooter
    ----------
    flux : np.array containing 2D-image flux
        Flux in input image
    error : np.array containing 2D-image error
        Error in input image
    binh : int
        binning along x-axis

    Returns
    -------
    binned fits image
    """

    print("Binning image by a factor: "+str(binh))
    if binh == 1:
        return wl, flux, error

    # Outsize
    size = flux.shape[0]
    outsize = int(np.round(size/binh))

    # Containers
    wl_out = np.zeros((outsize))
    res = np.zeros((outsize))
    reserr = np.zeros((outsize))

    for ii in np.arange(0, size - binh, binh):
        # Find psotions in new array
        h_slice = slice(ii, ii + binh)
        h_index = int((ii + binh)/binh) - 1
        # Construct weighted average and weighted std along binning axis
        res[h_index], reserr[h_index] = avg(flux[ii:ii + binh], error[ii:ii + binh], axis=0, weight=weight)
        wl_out[h_index] = np.ma.median(wl[ii:ii + binh], axis=0)

    return wl_out[1:-1], res[1:-1], reserr[1:-1]

#load final output and bin spectra
os.chdir(script_path+'/UVB/output/')

#UVB
waveU, fluxU, errU = np.loadtxt('UVB_ASCII1D_spectrum.dat', usecols=(0,1,2), unpack=True)
#bin
wU, fU, eU = bin_spectrum(waveU[2000:12600], fluxU[2000:12600], errU[2000:12600], 5, weight=True)

os.chdir(script_path+'/VIS/output/')

#VIS
waveV, fluxV, errV = np.loadtxt('VIS_ASCII1D_spectrum.dat', usecols=(0,1,2), unpack=True)
#bin
wV, fV, eV = bin_spectrum(waveV[1200:23500], fluxV[1200:23500], errV[1200:23500], 5, weight=True)

os.chdir(script_path+'/NIR/output/')

#NIR
waveN, fluxN, errN = np.loadtxt('NIR_ASCII1D_spectrum.dat', usecols=(0,1,2), unpack=True)
#bin
wN, fN, eN = bin_spectrum(waveN[300:], fluxN[300:], errN[300:], 3, weight=True)


#check plot
plt.figure()
plt.plot(wU,fU,'k-')
plt.plot(wV,fV,'k-')
plt.plot(wN,fN,'k-')
plt.xlim(3300,22000)
plt.show()

#export final spectra
f = open(script_path+'/output_bin.dat', 'w')
f.write('# air_wave      flux     error_flux\n')
for i in range(len(wU)):
    f.write('{:.4f}\t{:.4e}\t{:.4e}\n'.format(wU[i],fU[i],eU[i]))
for i in range(len(wV)):
    f.write('{:.4f}\t{:.4e}\t{:.4e}\n'.format(wV[i],fV[i],eV[i]))
for i in range(len(wN)):
    f.write('{:.4f}\t{:.4e}\t{:.4e}\n'.format(wN[i],fN[i],eN[i]))

f.close()
