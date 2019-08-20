from PIL import Image
from math import pow, ceil

def powerLawTransform(image,constant, gamma):
    
    pixelMap = image.load()

    for i in range(0,image.size[0]):
        for j in range(0,image.size[1]):
            pixelMap[i,j] = tuple( ceil( constant * pow(pixel, gamma)) for pixel in pixelMap[i, j])
    
    return image


image = Image.open('image.jpg')

powerLawTransform(image, int(input("Power Law Constant: ")), float(input("Gamma: "))).show()
