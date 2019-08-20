from PIL import Image

def addValue(image, value):
    pixelMap = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixelMap[i, j] = tuple( pix+val for pix,val in zip(pixelMap[i,j], value) )
    
    return image

image = Image.open('image.jpg')

addValue(image, (50, 50, 50)).show()
