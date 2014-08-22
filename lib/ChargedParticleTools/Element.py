from numpy import *


class Element:

	def __init__ (self,SymbolZ='H'):
		self.Path = '../data/ElementList.txt'
		Z = loadtxt(self.Path,skiprows=2,usecols=[0])
		Symbol = loadtxt(self.Path,skiprows=2,usecols=[1],dtype='str')
		Name = loadtxt(self.Path,skiprows=2,usecols=[2],dtype='str')
		ZA = loadtxt(self.Path,skiprows=2,usecols=[3])
		Ionization = loadtxt(self.Path,skiprows=2,usecols=[4]); # eV
		Density = loadtxt(self.Path,skiprows=2,usecols=[5]) # g/cm^3

		for i in range(len(Z)):
			if Symbol[i] == SymbolZ or Z[i] == SymbolZ:
				self.Z = Z[i]
				self.Symbol = Symbol[i]
				self.Name = Name[i]
				self.Ionization = Ionization[i]
				self.ZA = ZA[i]
				self.A = self.Z / ZA[i]
				self.Density = Density[i]

#Mo = Element('Mo')
