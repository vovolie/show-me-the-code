#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'vovo'

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook
import os

font = {
    'family' : 'serif',
    'color' : 'red',
    'weight' : 'bold',
    'size' : 26,

}
path = os.path.split(os.path.realpath(__file__))[0] + '/2.png'
image_file = cbook.get_sample_data(path)
image = plt.imread(image_file)
fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Circle((90, 90), radius=90, transform=ax.transData)
im.set_clip_path(patch)
plt.axis('off')
plt.text(160, 40, '12', fontdict=font)
plt.show()