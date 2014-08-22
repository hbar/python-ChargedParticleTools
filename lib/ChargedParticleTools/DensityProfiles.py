## DensityProfiles.py
## Dr. Harold Barnard and Jonathan Terry
## 8/21/2014

import numpy as np
import matplotlib.pyplot as plt

## Aggregation of various density profiles, maintaining the total density profile of
## the target material.
## Used for statistics management in simulation
class TargetRegion(object):

    def __init__(self, densityProfiles):

        self.densityProfiles = densityProfiles
        self.totalTargetLength = densityProfiles[0].totalTargetDistance
        self.interactions = []

    def recordReaction(self, depthIndex):
        totalNumberDensity = 0
        composition = {}

        for elem in self.densityProfiles:
            name = elem.name
            numberDensity = elem.profileRange[depthIndex]
            totalNumberDensity += numberDensity

            if (name in composition):
                composition[name] += numberDensity
            else:
                composition[name] = numberDensity

        print "REACTION RECORDED AT " + str(depthIndex/100.0)
        print "Element\t Percentage\n"
        for elem in composition.keys():
            composition[elem] = 100*composition[elem]/totalNumberDensity
            if (composition[elem] > .001):
                print elem + "\t" + str(composition[elem]) + "\n" 

    def visualizeTotalTarget(self):

        frame, fig = plt.subplots()
        
        for elem in self.densityProfiles:
            fig.plot(elem.profileDomain, elem.profileRange, label = elem.regionName)

        legend = fig.legend(loc = 'upper right', shadow = True)
        plt.title('Target Density Profile')
        plt.xlabel('Target Depth')
        plt.ylabel('Number Densities in Target')
        plt.show()



## Supports the creation of either gaussian or step function density 
## distributions. Across a target region (compilation of density profiles)
## the totalTargetDistance must be constant.

## totalTargetDistance = total thickness of target
## regionName = name of region (used for statistical analysis)
## regionSymbol = symbol for element that region is made of
## shape = shape of desired number density distribution (either Gaussian or recangular)
## mu = average of Gaussian OR center of rectangle
## sigma = standard dev of Gaussian OR half width of recatngle
## scale = maximum number density of distribution
## edgeTolerance = standard dev of Gaussian used to smooth rectangular distributions 

class DensityProfile(object):

    def __init__(self, totalTargetDistance, regionName, regionSymbol, shape, mu, sigma, scale, edgeTolerance = 1):

        self.profileDomain = np.linspace(0, totalTargetDistance, 10000)
        self.totalTargetDistance = totalTargetDistance
        self.regionName = regionName

        with open('Universal Data Table.txt') as elementData:
            for line in elementData.readlines()[5:]:
                line.strip()
                col0, col1, col2, col3, col4, col5 = line.split()

                if (regionSymbol == col1):
                    self.atomicNumber = int(col0)
                    self.symbol = col1
                    self.name = col2
                    self.atomicMass = int(col0)/float(col3)
                    self.meanIonization = float(col4)
                    self.density = float(col5)
                    break

        if (shape == 'Gaussian'):
            gaussScale = scale*sigma*np.sqrt(2*np.pi)
            self.profileRange = self.gaussian(self.profileDomain, mu, sigma, gaussScale)

        else:
            self.profileRange = self.rectangle(self.profileDomain, mu, sigma, scale)
            self.smooth(mu, sigma, scale, edgeTolerance)

    def smooth(self, mu, sigma, scale, edgeTolerance):

        gaussScale = scale*edgeTolerance*np.sqrt(2*np.pi)
        self.profileContourSubtract('Gaussian', mu-sigma, edgeTolerance, gaussScale)
        self.profileContourSubtract('Gaussian', mu+sigma, edgeTolerance, gaussScale)

    def profileContourAdd(self, shape, mu, sigma, scale):

        if (shape == 'Gaussian'):
            appendage = self.gaussian(self.profileDomain, mu, sigma, scale)
            self.profileRange = self.profileRange + appendage

        else:
            appendage = self.rectangle(self.profileDomain, mu, sigma, scale)
            self.profileRange = self.profileRange + appendage

    def profileContourSubtract(self, shape, mu, sigma, scale):

        if (shape == 'Gaussian'):
            appendage = self.gaussian(self.profileDomain, mu, sigma, scale)
            self.profileRange = self.profileRange - appendage
            np.clip(self.profileRange, 0, np.inf, out = self.profileRange)

        else:
            appendage = self.rectangle(self.profileDomain, mu, sigma, scale)
            self.profileRange = self.profileRange - appendage
            np.clip(self.profileRange, 0, np.inf, out = self.profileRange)

    def addProfile(self, profile):

        self.profileRange = self.profileRange + profile.profileRange

    def subtractProfile(self, profile):

        self.profileRange = self.profileRange - profile.profileRange

    def gaussian(self, x, mu, sigma, scale):

        scaledNormalization = scale/np.sqrt(2*np.pi*sigma*sigma)
        gaussian = lambda i: scaledNormalization*np.exp(-((i-mu)**2)/(2*sigma**2))
        return np.array([gaussian(i) for i in x])

    def rectangle(self, x, mu, sigma, scale):

        heaviside = lambda i: scale if (i > (mu-sigma) and i < (mu+sigma)) else 0
        return np.array([heaviside(i) for i in x])

    def visualize(self):
        print "REGION SELECTED: " + self.regionName
        print "Displaying distribution for " + self.name + " in a " + str(self.totalTargetDistance) + " micron target."
        
        plt.xlabel('Target Depth')
        plt.ylabel(self.name + " Number Density in Target")
        plt.plot(self.profileDomain, self.profileRange)
        plt.show()

