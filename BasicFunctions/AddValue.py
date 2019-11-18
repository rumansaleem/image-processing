from PIL import Image
import numpy as np

def addValue(image, value):
    pixelMap = np.asarray(np.asarray(image), np.uint8)
    newPixelMap = np.add(pixelMap, value)
    newPixelMap[newPixelMap > 255] = 255
    newPixelMap[newPixelMap < 0] = 0

    return Image.fromarray(newPixelMap.astype(np.uint8))

image = Image.open('image.jpg')

image.show()
addValue(image, np.asarray((90, 50, 50))).show()
