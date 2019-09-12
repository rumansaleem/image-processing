from PIL import Image
from matplotlib import pyplot

def intensitiesRGBMap(image):
    pixelMap = image.load()

    map = {
        'red': [i for i in range(0, 256)],
        'blue': [i for i in range(0, 256)],
        'green': [i for i in range(0, 256)],
    }

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            red, green, blue = pixelMap[i,j]
            map['red'][red] += 1
            map['green'][green] += 1
            map['blue'][blue] += 1

    return map

image = Image.open('image.jpg')
image.show()
rgbHistogram = intensitiesRGBMap(image)

pyplot.bar(list(range(256)), rgbHistogram['red'], color='#ff0000AA')
pyplot.bar(list(range(256)), rgbHistogram['green'], color='#00ff0088')
pyplot.bar(list(range(256)), rgbHistogram['blue'], color='#0000ff77')
pyplot.show()