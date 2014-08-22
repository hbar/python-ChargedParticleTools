## Detector.py
## Dr. Harold Barnard and Jonathan Terry
## 8/22/2014


class Detector(object):

    def __init__(self, area, x, y):

        self.x = x
        self.y = y
        self.area = area

    def getSolidAngle(self, interaction):

        (interactionX, interactionY) = interaction.getCoordinates
        xPrime = np.abs(self.x - interactionX)
        yPrime = np.abs(self.y - interactionY)

        radiusSquared = xPrime**2 + yPrime**2
        radius = np.sqrt(radiusSquared)

        solidAngle = self.area/radiusSquared

        return (radius, solidAngle)