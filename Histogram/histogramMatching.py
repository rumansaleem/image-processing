from PIL import Image
from matplotlib import pyplot
import numpy as np
from functools import reduce

class HistogramMatcher:
    def __init__(self, pathToImage):
        self.image = Image.open(pathToImage).convert('L')

    def histogram(self, image = None):
        if image == None:
            image = self.image
        return np.bincount(np.asarray(image, np.uint8).flatten())

    def pDistributionFunction(self, histogram = None):
        if not isinstance(histogram, np.ndarray):
            histogram = self.histogram()

        LEVELS = len(histogram)
        TOTAL_PIXELS = sum(histogram)

        return [round((count / TOTAL_PIXELS) * LEVELS) for count in histogram]

    def cDistributionFunction(self, pdf = None):
        if pdf == None:
            pdf = self.pDistributionFunction()

        LEVELS = len(pdf)

        return [
            reduce(lambda prev, curr: prev + curr, pdf[0:i + 1])
            for i in range(0, LEVELS + 1)
        ]

    def equalize(self):
        cdf = self.cDistributionFunction()
        pixelMap = self.image.load()

        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                pixelMap[i, j] = cdf[pixelMap[i, j]]

    def matchLevel(self, referenceCDF, level):
        originalCDF = self.cDistributionFunction()
        levelOriginalCount = originalCDF[level]

        filtered = [enum for enum in enumerate(referenceCDF) if enum[1] >= levelOriginalCount] 

        if len(filtered) < 1:
            return level

        outputLevel, _ = min(filtered, key=lambda x: abs(x[1]-levelOriginalCount))

        return outputLevel

    def performMatching(self, referenceImage):
        referenceHist = self.histogram(referenceImage)
        referencePDF = self.pDistributionFunction(referenceHist)
        referenceCDF = self.cDistributionFunction(referencePDF)

        return [
            self.matchLevel(referenceCDF, level)
            for level in range(0, 256)
        ]

    def applyMapping(self, mapping, show=False):
        pixelMap = self.image.load()

        for i in range(0, self.image.size[0]):
            for j in range(0, self.image.size[1]):
                pixelMap[i, j] = mapping[pixelMap[i, j]]
                
        if show :
            self.image.show()


referenceImage = Image.open('reference.jpg').convert('L')
matcher = HistogramMatcher('goldengate.jpg')
mapping = matcher.performMatching(referenceImage)

print(mapping)

matcher.applyMapping(mapping, show=True)
