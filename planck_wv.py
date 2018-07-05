import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

def planck_wv(T,wv):
        #
        # This is a python script that calculates the Planck radiance
        # given 1-by-N vectors of temperature (T) in Kelvin and
        # wavelengths (wv) in um.  The radiance (radiance) is in
        # W m-2 sr-1 um-1.
        # Written by: Von Walden
        #            13 January 1998
        # addpted to python by shahar weksler
        #             21/07/2016

    # row_T ,col_T  = T.shape
    # # [row_wv,col_wv = wv.shape
    #
    # if row_T != 1: #or row_wv != 1
    #    print ('One of the input vectors is NOT a column vector.')
    #    print ('Try again!')

    h = const.h
    c = const.c
    k = const.k

    wv2 = wv * 1e-6
    numer = ((2.*h*c*c) / ( wv2 ** 5) )
    denom = np.exp(h * c / (k * T * wv2)) - 1.
    radiance = numer/ denom

    return radiance

##################################################import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

def planck_wv(T,wv):
        #
        # This is a python script that calculates the Planck radiance
        # given 1-by-N vectors of temperature (T) in Kelvin and
        # wavelengths (wv) in um.  The radiance (radiance) is in
        # W m-2 sr-1 um-1.
        # Written by: Von Walden
        #            13 January 1998
        # addpted to python by shahar weksler
        #             21/07/2016

    # row_T ,col_T  = T.shape
    # # [row_wv,col_wv = wv.shape
    #
    # if row_T != 1: #or row_wv != 1
    #    print ('One of the input vectors is NOT a column vector.')
    #    print ('Try again!')

    h = const.h
    c = const.c
    k = const.k

    wv2 = wv * 1e-6
    numer = ((2.*h*c*c) / ( wv2 ** 5) )
    denom = np.exp(h * c / (k * T * wv2)) - 1.
    radiance = numer/ denom

    return radiance

###################################################################
        # insert one spectra X and wavelengths WV
        # output L - Planck Spectra and T - Temp in Kelvin (single value)
def create_planck_arrays(T,wv):
    planck_array = []
    for t in T:
        planck_array.append(planck_wv(t, wv))
        planck_array1 = np.array(planck_array)
    return planck_array1

def planckFitting(radiance_img, wv):
    if radiance_img.mean() != 0:
        # planck_array = []
        T = np.arange(373.15, 273.0, -5.0)
        planck_array1 = create_planck_arrays(T,wv)

        # insert plancks to Planckmat matrix
        # for t in T:
        #     planck_array.append(planck_wv(t, wv))
        #     planck_array1 = np.array(planck_array)

        # find index of first occurence where planck curve is lower than spectra
        # first = np.where(sum(planck_array1 > radiance_img))
        # first = np.where(sum((planck_array) < np.tile(np.transpose(radiance_img), (0, 20))) != 0)

        j = 0
        while sum(planck_array1[j, :] < radiance_img) == 0 and j < planck_array1.shape[0]:
           j += 1
        first = j

        Temperature_first = T[(first-1)] # go one index up
        T = np.arange(Temperature_first, Temperature_first - 5.1, -0.1) # build 50 planck spectra between 5 degrees in 0.1 intervals
        planck_array = []
        for t in T:
            planck_array.append(planck_wv(t, wv))
            planck_array2 = np.array(planck_array)
        # first = find(sum(np.transpose(planck_array)< np.tile(np.transpose(radiance_img), [1, 49])) != 0, 1)
        # first = np.where(sum(planck_array2 > radiance_img))
        j = 0
        while sum(planck_array2[j, :] < radiance_img) == 0 and j < planck_array2.shape[0]:
            j += 1
        first = j
        Temperature_final = T[first]
        L = planck_array2[first, :]
    else:
        Temperature_final = 0
        L = radiance_img
    return L, Temperature_final
#################
        # insert one spectra X and wavelengths WV
        # output L - Planck Spectra and T - Temp in Kelvin (single value)
def create_planck_arrays(T,wv):
    planck_array = []
    for t in T:
        planck_array.append(planck_wv(t, wv))
        planck_array1 = np.array(planck_array)
    return planck_array1

def planckFitting(radiance_img, wv):
    if radiance_img.mean() != 0:
        # planck_array = []
        T = np.arange(373.15, 273.0, -5.0)
        planck_array1 = create_planck_arrays(T,wv)

        # insert plancks to Planckmat matrix
        # for t in T:
        #     planck_array.append(planck_wv(t, wv))
        #     planck_array1 = np.array(planck_array)

        # find index of first occurence where planck curve is lower than spectra
        # first = np.where(sum(planck_array1 > radiance_img))
        # first = np.where(sum((planck_array) < np.tile(np.transpose(radiance_img), (0, 20))) != 0)

        j = 0
        while sum(planck_array1[j, :] < radiance_img) == 0 and j < planck_array1.shape[0]-1:
           j +=1
        first = j

        Temperature_first = T[(first-1)] # go one index up
        T = np.arange(Temperature_first, Temperature_first - 5.0, -0.1) # build 50 planck spectra between 5 degrees in 0.1 intervals
        planck_array = []
        for t in T:
            planck_array.append(planck_wv(t, wv))
            planck_array2 = np.array(planck_array)
        # first = find(sum(np.transpose(planck_array)< np.tile(np.transpose(radiance_img), [1, 49])) != 0, 1)
        # first = np.where(sum(planck_array2 > radiance_img))
        j = 0
        while sum(planck_array2[j, :] < radiance_img) == 0 and j < planck_array2.shape[0]-1:
            j += 1
        first = j
        Temperature_final = T[first]
        L = planck_array2[first, :]
    else:
        Temperature_final = 0
        L = radiance_img
    return L, Temperature_final
