from numpy import *


class Element(object):

	def __init__ (self,SymbolZ='H'):
		self.path = '../data/ElementList.txt'
		Z = loadtxt(self.path,skiprows=2,usecols=[0])
		Symbol = loadtxt(self.path,skiprows=2,usecols=[1],dtype='str')
		Name = loadtxt(self.path,skiprows=2,usecols=[2],dtype='str')
		ZA = loadtxt(self.path,skiprows=2,usecols=[3])
		Ionization = loadtxt(self.path,skiprows=2,usecols=[4]); # eV
		Density = loadtxt(self.path,skiprows=2,usecols=[5]) # g/cm^3

		for i in range(len(Z)):
			if Symbol[i] == SymbolZ or Z[i] == SymbolZ:
				self.z = Z[i]
				self.symbol = Symbol[i]
				self.name = Name[i]
				self.ionization = Ionization[i]
				self.a = self.z / ZA[i]
				self.density = Density[i]

#Mo = Element('Mo')
