from PIL import Image
from math import ceil, log

def logTransform(image, constant):
    '''
    Implement log transformation
    r = c * log(i+1)
    '''

    pixelMap = image.load()

    for i in range(0,image.size[0]):
        for j in range(0,image.size[1]):
            pixelMap[i,j] = tuple( ceil(constant * log(pixel + 1)) for pixel in pixelMap[i, j] )

    return image


image = Image.open('image.jpg')

logTransform(image, int(input('Log Transform Constant: '))).show()
