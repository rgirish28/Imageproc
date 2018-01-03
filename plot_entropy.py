"""
=======
Entropy
=======

In information theory, information entropy is the log-base-2 of the number of
possible outcomes for a message.

For an image, local entropy is related to the complexity contained in a given
neighborhood, typically defined by a structuring element. The entropy filter can
detect subtle variations in the local gray level distribution.

In the first example, the image is composed of two surfaces with two slightly
different distributions. The image has a uniform random distribution in the
range [-14, +14] in the middle of the image and a uniform random distribution in
the range [-15, 15] at the image borders, both centered at a gray value of 128.
To detect the central square, we compute the local entropy measure using a
circular structuring element of a radius big enough to capture the local gray
level distribution. The second example shows how to detect texture in the camera
image using a smaller structuring element.

"""
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from PIL import Image

from skimage import data
from skimage.util import img_as_ubyte
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters.rank import gradient

# First example: object detection.

# Second example: texture detection.


path = '/Users/rgirish28/Documents/Strip JPEGs/'

image1 = Image.open(os.path.join(path,sys.argv[1]))


image = img_as_ubyte(image1)

image = image[:,:,1]

fig, (ax0, ax1) = plt.subplots(ncols=2, sharex=True,
                               sharey=True,
                               subplot_kw={"adjustable": "box-forced"})

img0 = ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title("Image")
ax0.axis("off")
fig.colorbar(img0, ax=ax0)

img1 = ax1.imshow(gradient(image, disk(5)), cmap=plt.cm.jet)
ax1.set_title("Entropy")
ax1.axis("off")
fig.colorbar(img1, ax=ax1)

fig.tight_layout()

plt.show()
