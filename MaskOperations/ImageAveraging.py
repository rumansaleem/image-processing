from PIL import Image
import numpy as np
from functools import reduce


def averaging(images):
    pixelMaps = [ np.asarray(image) for image in images ]
    newPixelMap = np.average(pixelMaps, axis=0)
    return Image.fromarray(newPixelMap.astype(np.uint8))


image1 = Image.open('goldengate_noisy.jpg').convert('L')
image2 = Image.open('goldengate_noisy2.jpg').convert('L')

image1.show()
image2.show()

averaging([image1, image2]).show()