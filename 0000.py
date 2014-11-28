__author__ = 'vovo'


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

font = {
    'family' : 'serif',
    'color' : 'red',
    'weight' : 'bold',
    'size' : 26,

}
image_file = cbook.get_sample_data('/home/vovo/show-me-the-code/show-me-the-code/1.jpg')
image = plt.imread(image_file)
fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Circle((90, 90), radius=90, transform=ax.transData)
im.set_clip_path(patch)
plt.axis('off')
plt.text(160, 40, '12', fontdict=font)
plt.show()