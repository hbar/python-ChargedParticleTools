## Implementation of the bethe bloch equation to calculate stopping power for ions

from numpy import *
from Constants import *

class IonStoppingCrossSection(object):

	def __init__(self,target,ion):

		Zt = target.z
		self.target = target
		self.ion = ion
		self.C0 = ( ((q0**2)/(4.0*pi*ep0))**2 )
		self.C1 = ( (4.0 * pi * ion.z**2 * Zt )/(me*q0) )
		self.C2 = ( 2.0 * me / (target.ionization ) )


	def sigmaE(self,energy):
		T = array(energy)
		gamma = 1.0 + T/self.ion.m0
		beta = sqrt(1.0-1.0/gamma**2)
		SigmaE = self.C0 * (self.C1/beta**2) * ( log(self.C2 * beta**2) - log(1.0-beta) - beta**2 )
		return SigmaE


