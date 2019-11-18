from PIL import Image
import numpy as np

def invertImage(image):
    pixelMap = np.asarray(image, np.uint8)
    
    pixelMap = np.subtract(255, pixelMap)
    
    return Image.fromarray(pixelMap)

image = Image.open('image.jpg')

invertImage(image).show()


