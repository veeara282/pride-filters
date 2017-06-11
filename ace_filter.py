# An Asexual Pride Filter
# 
# Copyright (C) 2017 Aidan Fitzgerald
# Source: https://commons.wikimedia.org/wiki/File:Asexual_flag.svg

import numpy as np
from scipy.misc import imread, imshow, imsave
from sys import argv, exit
from chunk import *


# Get filename from command line
if len(argv) > 1:
    filename = argv[1]
else:
    print("Usage: python3 ace_filter.py [filename]")
    exit(2)

# Read image
# We need to upcast it to 16-bit so we can store intermediate values greater than 255
image = imread(filename).astype(np.uint16)

print(image.dtype)

stripes = chunk(image, 4)

for stripe in stripes:
    print(stripe.shape)

black = np.array([0, 0, 0], dtype=np.uint16) #000000
gray = np.array([163, 163, 163], dtype=np.uint16) #a3a3a3
white = np.array([255, 255, 255], dtype=np.uint16) #ffffff
purple = np.array([128, 0, 128], dtype=np.uint16) #800080

stripes[0] += black
stripes[1] += gray
stripes[2] += white
stripes[3] += purple

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
