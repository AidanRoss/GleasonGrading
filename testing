import skimage
import glob
import numpy as np
from skimage.color import rgb2hed
from skimage.filters.thresholding import threshold_otsu
import matplotlib.pyplot as plt
import skimage.io
import os, errno


# Declare path the extracted TMA core Images
image_path = "\Users\Aidan\Desktop\Fourth Year\First Semester\ENPH 455 - Thesis\Extracted Cores\\19.tif"
im = image_path
# image_path = '1.tif'


ihc_rgb = skimage.io.imread(im)
ihc_he = rgb2hed(ihc_rgb)
h_channel = ihc_he[:, :, 0]
e_channel = ihc_he[:, :, 1]


h_thresh = threshold_otsu(h_channel)
e_thresh = threshold_otsu(e_channel)
h_bin = (h_channel > h_thresh)
e_bin = (e_channel > e_thresh)

plt.figure(1)
plt.imshow(h_channel, cmap='gray')
plt.figure(2)
plt.imshow(e_channel, cmap='gray')
plt.figure(3)
plt.imshow(h_bin, cmap='gray')
plt.figure(4)
plt.imshow(e_bin, cmap='gray')

plt.show()

filename1 = 'Saved_Images/H_19.png'  # 'Labelled_%s' % + ".png"  # '%s' % img
filename2 = 'Saved_Images/E_19.png'
filename3 = 'Saved_Images/H_bin19.png'
filename4 = 'Saved_Images/E_bin19.png'

if not os.path.exists(os.path.dirname(filename1)):
    try:
        os.makedirs(os.path.dirname(filename1))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filename1, "w") as f:
    f.write(filename1)
plt.imsave(fname=filename1, arr=h_channel, cmap='gray')

if not os.path.exists(os.path.dirname(filename2)):
    try:
        os.makedirs(os.path.dirname(filename2))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filename2, "w") as f:
    f.write(filename2)
plt.imsave(fname=filename2, arr=e_channel, cmap='gray')

if not os.path.exists(os.path.dirname(filename3)):
    try:
        os.makedirs(os.path.dirname(filename3))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filename3, "w") as f:
    f.write(filename3)
plt.imsave(fname=filename3, arr=h_bin, cmap='gray')

if not os.path.exists(os.path.dirname(filename4)):
    try:
        os.makedirs(os.path.dirname(filename4))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filename4, "w") as f:
    f.write(filename4)
plt.imsave(fname=filename4, arr=e_bin, cmap='gray')
