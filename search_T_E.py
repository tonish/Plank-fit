
'''
this code reads:
1) an ENVI format radiance image
2) an ASCII spectrum file with the same spectral resolution
it then runs a search for the best fitting planck function for each
pixel in the radiance image. the output is:
1) a spectral cube containing the best fitted planck function
of every pixel (ENVI image format);
2) a temperature image icln K degrees (ENVI image format)
...
Created by Offer Rozenstein using MATLAB R2011b
updated for MATLAB 2015a on 8-July-2015
update for python on 21/7/2016
'''

import planck_wv
import TK
import spectral as sp
import numpy

# input file
filename = TK.get_file([('all formats', '.*')], 'select radiance image file') #open  radiance image
# #read input
radiance_img = sp.envi.open((filename[:-4] + '.hdr'), filename)


ImageSampleNumber = radiance_img.shape[0]
ImageVarNumber = radiance_img.shape[1]
ImageBandsNumber = radiance_img.shape[2]

radiance_img_squeezed = radiance_img.load().reshape((ImageSampleNumber*ImageVarNumber, ImageBandsNumber))

row_img_squeezed = radiance_img_squeezed.shape[0]
col_img_squeezed = radiance_img_squeezed.shape[1]

planck = []
temp = []

for i in range(row_img_squeezed):
    L, T = planck_wv.planckFitting(radiance_img_squeezed[i, :], numpy.array(radiance_img.bands.centers))
    planck.append(L)
    temp.append(T)
    print float(i)/float(row_img_squeezed)
planck1 = numpy.array(planck)
temp1 = numpy.array(temp)

BB = planck1.reshape((ImageSampleNumber, ImageVarNumber, ImageBandsNumber))
Temperature = temp1.reshape(ImageSampleNumber , ImageVarNumber)
radiance_img.metadata.keys()
# """"""
# #writing to files
# """"""
# #save planck curve image
# Planck_name = os.path.split(filename)[1][:-3]
# hdr = sp.envi.read_envi_header()
hdr_name = filename[:-4] + '.hdr'
hdr = sp.envi.read_envi_header(hdr_name)
planck_save_name = filename[:-4] + '_planck' + '.hdr'
sp.envi.save_image(planck_save_name, BB, dtype=numpy.float32, ext = '', interleave = 'bip', metadata = hdr, force = True)

# saving the temperature image
temperature_save_name = filename[:-4] + '_Temperature' + '.hdr'
temperature_hdr = hdr

del temperature_hdr['wavelength']
del temperature_hdr['fwhm']

sp.envi.save_image(temperature_save_name, Temperature, dtype=numpy.float32, ext = '', interleave = 'bip', metadata = temperature_hdr, force = True)
