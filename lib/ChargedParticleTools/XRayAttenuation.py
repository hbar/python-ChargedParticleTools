from numpy import *
import pylab as pl

TestRange=logspace(-8,-4,1000)

class Attenuation:
	def __init__(self,Z=42):
		self.Path0 = '../data/XRayAttenuation/'
		self.FileName = str(Z)+'XRayAttenuation.txt'
		self.Data = genfromtxt(self.Path0+self.FileName,skiprows=11)
		self.Energy = self.Data[:,0]*1e6
		self.Mu = self.Data[:,1] # cm^2/g
		self.MuEnergy = self.Data[:,2] # cm^2/g
		self.Label='Z = '+ str(Z)

	def PlotAttenuation(self):
		pl.loglog(self.Energy,self.Mu,label=self.Label)
		pl.xlabel('Energy [eV]')
		pl.ylabel(r'Mass Attenuation Coefficient [cm$^2$/g]')

	def MeanFreePath(self,Rho=10.28,Plot=True):
		self.MFP = 1.0/(Rho*self.Mu) * 1e-2
		if Plot==True:
			pl.loglog(self.Energy,self.MFP)
			pl.xlabel('Energy [eV]')
			pl.ylabel('Mean Free Path [m]')

	def MuValue(self,PhotonE):
		return interp(PhotonE,self.Energy,self.Mu)

	def Intensity(self,PhotonE=3e3, Rho=10.28, Distance=TestRange,Plot=True):
		MuRho = self.MuValue(PhotonE)
		IAtten = exp(-MuRho*Rho*Distance*100.0)
		if Plot==True:
#			pl.loglog(Distance,IAtten)
			pl.semilogx(Distance,IAtten)
		return IAtten
		

