from numpy import *
import pylab as pl
from Element import *

TestRange=logspace(-8,-4,1000)

class Attenuation(object):
    def __init__(self,Z=42):
        self.element = Element(Z)
        self.path0 = '../data/XRayAttenuation/'
        self.fileName = str(Z)+'XRayAttenuation.txt'
        self.data = genfromtxt(self.Path0+self.fileName,skiprows=11)
        self.energy = self.data[:,0]*1e6
        self.mu = self.data[:,1] # cm^2/g
        self.muEnergy = self.data[:,2] # cm^2/g
        self.label= self.element.Symbol #'Z = '+ str(Z)

    def PlotAttenuation(self):
        pl.loglog(self.energy,self.mu,label=self.label)
        pl.xlabel('Energy [eV]')
        pl.ylabel(r'Mass Attenuation Coefficient [cm$^2$/g]')

    def MeanFreePath(self,Rho=10.28,Plot=True):
        self.mfp = 1.0/(Rho*self.mu) * 1e-2
        if Plot==True:
            pl.loglog(self.energy,self.mfp,label=self.label)
            pl.xlabel('Energy [eV]')
            pl.ylabel('Mean Free Path [m]')

    def MuValue(self,PhotonE):
        return interp(PhotonE,self.energy,self.Mu)

    def Intensity(self,PhotonE=3e3, Rho=10.28, Distance=TestRange,Plot=True):
        MuRho = self.muValue(PhotonE)
        IAtten = exp(-MuRho*Rho*Distance*100.0)
        if Plot==True:
#           pl.loglog(Distance,IAtten)
            pl.semilogx(Distance,IAtten)
            pl.xlabel('Distance [m]')
            pl.ylabel('Relative Intensity [I/Io]')
        return Distance,IAtten
        

