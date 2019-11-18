from PIL import Image
import numpy as np

def performAnd(image, mask):
    return np.bitwise_and(image, mask)

def performOr(image, mask):
    return np.bitwise_or(image, mask)


image = Image.open('goldengate.jpg').convert('L')

imageArray = np.asarray(image, 'uint8')
mask = np.zeros(imageArray.shape, 'uint8')
mask[50:200, 150:350] = 255

andImageArray = performAnd(imageArray, mask)
orImageArray = performOr(imageArray, mask)

Image.fromarray(andImageArray).show()
Image.fromarray(orImageArray).show()
