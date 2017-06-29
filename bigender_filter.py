# A Bigender Pride Filter
# 
# Copyright (C) 2017 Aidan Fitzgerald

import numpy as np
from scipy.misc import imread, imshow, imsave
from sys import argv, exit
from chunk import *


# Get filename from command line
if len(argv) > 1:
    filename = argv[1]
else:
    print("Usage: python3 gnc_filter.py [filename]")
    exit(2)

# Read image
# We need to upcast it to 16-bit so we can store intermediate values greater than 255
image = imread(filename).astype(np.uint16)

print(image.dtype)

stripes = chunk(image, 7)

for stripe in stripes:
    print(stripe.shape)

# Bigender flag colors: c479a0, eca6cb, d5c7e8, ffffff, d5c7e8, 9ac7e8, 6c83cf
dark_pink = np.array([196, 121, 160], dtype=np.uint16) #c479a0
light_pink = np.array([236, 166, 203], dtype=np.uint16) #eca6cb
light_purple = np.array([213, 199, 232], dtype=np.uint16) #d5c7e8
white = np.array([255, 255, 255], dtype=np.uint16) #ffffff
# light_purple again
light_blue = np.array([154, 199, 232], dtype=np.uint16) #9ac7e8
dark_blue = np.array([108, 131, 207], dtype=np.uint16) #6c83cf

stripes[0] += dark_pink
stripes[1] += light_pink
stripes[2] += light_purple
stripes[3] += white
stripes[4] += light_purple
stripes[5] += light_blue
stripes[6] += dark_blue

for stripe in stripes:
    stripe = np.floor_divide(stripe, 2)

# Unchunk
transfm_img = unchunk(stripes)#.astype(np.uint8)
# Tried converting back to 8-bit, but it screws up the colors

print(transfm_img.shape)

# For debugging purposes
# imshow(transfm_img)

# Create output filename
def output_fname(fname):
    # Split into filename, '.', extension
    parts = fname.rpartition('.')
    # Add '.out' before extension
    return parts[0] + '.out.' + parts[2]

imsave(output_fname(filename), transfm_img)
