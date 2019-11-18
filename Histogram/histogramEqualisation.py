from PIL import Image
from matplotlib import pyplot
from functools import reduce

def intensitiesGrayMap(image):
    pixelMap = image.load()

    intensities = [0 for i in range(0, 256)]
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            gray = pixelMap[i, j]
            intensities[gray] += 1

    return intensities



def equalizeHistogram(image):
    totalPixels  = image.size[0] * image.size[1]
    levels = 255
    pdf = [ round((freq/totalPixels)*levels) for freq in intensitiesGrayMap(image)]
    cdfTransform = [ reduce(lambda prev, curr: prev+curr, pdf[0:i+1]) for i in range(0, levels+1)]
    pixelMap = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixelMap[i, j] = cdfTransform[pixelMap[i, j]]

image = Image.open('goldengate.jpg')
image.show()
equalizeHistogram(image)
image.show()