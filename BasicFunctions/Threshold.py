from PIL import Image
import numpy as np

def applyThreshold(image, threshold = 127):
    pixelMap = np.asarray(image)
    newPixelMap = np.zeros(pixelMap.shape)
    newPixelMap[pixelMap <= threshold] = 0
    newPixelMap[pixelMap > threshold] = 255
    return Image.fromarray(newPixelMap)

image = Image.open('goldengate.jpg').convert('L')
t = int(input('Threshold Value: '))
applyThreshold(image, t).show()