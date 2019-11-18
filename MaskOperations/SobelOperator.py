from PIL import Image
import numpy as np

def addFilter(image, filterImage, constant=1):
    pixelMap = np.asarray(image, np.uint16) + np.asarray(
        filterImage, np.uint16)
    pixelMap[pixelMap < 0] = 0
    pixelMap[pixelMap > 255] = 255
    return Image.fromarray(pixelMap.astype(np.uint8))

def applyOperator(pixelMap, operator):
    size = operator.shape[0]
    padding = size-2 if size > 2 else 0

    pixelMap = np.pad(pixelMap, (padding, padding)).astype(np.int)

    newPixelMap = np.zeros(pixelMap.shape, dtype=np.int)

    start = (size - 1) // 2
    end = size // 2
    print([padding, start, end])

    for i in range(start, pixelMap.shape[0] - end):
        for j in range(start, pixelMap.shape[1] - end):
            submatrix = pixelMap[i - start:i + end +1, j - start:j + end + 1]
            newPixelMap[i, j] = np.sum(np.multiply(submatrix, operator))

    newPixelMap[newPixelMap <= 0] = 0
    newPixelMap[newPixelMap >= 255] = 255

    if padding > 0:
        newPixelMap = newPixelMap[padding:-padding,padding:-padding]

    return newPixelMap


def sobelFilter(image, axis="x"):
    pixelMap = np.asarray(image, np.int)

    operators = {
        "x": np.asarray([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ], np.int),
        "y": np.asarray([
            [ 1,  2,  1],
            [ 0,  0,  0],
            [-1, -2, -1],
        ], np.int),
    }
    newPixelMap = applyOperator(pixelMap, operators[axis])
    return Image.fromarray(newPixelMap.astype(np.uint8))


image = Image.open('goldengate.jpg').convert('L')
sobelFilter(image, 'x').show()
sobelFilter(image, 'y').show()
# sharpendImage = addFilter(image, sobelFilterMask)
# sobelFilterMask.show()
# sharpendImage.show()