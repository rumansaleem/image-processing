from PIL import Image

def invertImage(image):
    pixelMap = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixelMap[i, j] = tuple( 255-value for value in pixelMap[i, j] )
    
    return image

image = Image.open('image.jpg')

invertImage(image).show()


