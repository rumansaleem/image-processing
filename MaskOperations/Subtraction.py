from PIL import Image
import numpy as np

def subtraction(image1, image2):
    pixelMap1 = np.asarray(image1, np.uint8)
    pixelMap2 = np.asarray(image2, np.uint8)

    newPixelMap = np.subtract(pixelMap1, pixelMap2)
    newPixelMap[newPixelMap < 0] = 0

    return Image.fromarray(newPixelMap.astype(np.uint8))



image1 = Image.open('image.jpg').convert('L')
image2 = Image.open('reference.jpg').convert('L')\
    .resize((image1.size[0], image1.size[1]), Image.LANCZOS)

image1.show()
image2.show()

subtraction(image1, image2).show()