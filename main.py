import skimage
import glob
import numpy as np
from skimage.color import rgb2hed
from skimage.filters.thresholding import threshold_otsu
import matplotlib.pyplot as plt
import skimage.io


# Declare path the extracted TMA core Images
image_path = "\Users\Aidan\Desktop\Fourth Year\First Semester\ENPH 455 - Thesis\Extracted Cores"
# image_path = '1.tif'
img_files = glob.glob(image_path + '\\*.tif')
print img_files
num_image = len(img_files)
for im in img_files:
    ihc_rgb = skimage.io.imread(im)

    ihc_he = rgb2hed(ihc_rgb)

    h_channel = ihc_he[:, :, 0]
    e_channel = ihc_he[:, :, 1]

    h_thresh = threshold_otsu(h_channel)
    e_thresh = threshold_otsu(e_channel)

    h_bin = (h_channel > h_thresh)
    e_bin = (e_channel > e_thresh)

    plt.figure(1)
    plt.title('Hematoxylin Channel')

    plt.subplot(121)
    plt.imshow(h_channel, cmap='gray')
    plt.subplot(122)
    plt.imshow(h_bin, cmap='gray')

    plt.figure(2)
    plt.title('Eosin Channel')

    plt.subplot(121)
    plt.suptitle('test')
    plt.imshow(e_channel, cmap='gray')

    plt.subplot(122)
    plt.imshow(e_bin, cmap='gray')

    plt.show()

