from numpy import *

TestFile= '../data/Hydrogen in Boron SRIM Data.txt'

class SRIMData:

	def __init__(self,FileName=TestFile):
#		File = open(FileName,'r')
		self.RowLimits = []
		linenumber = 1
		with open(FileName) as f:
		    for line in f:
				if line[0] == '-':
					self.RowLimits.append(linenumber)
				linenumber=linenumber+1
		self.RowMax = linenumber
		Header=self.RowLimits[0]-1
		Footer = self.RowMax-self.RowLimits[1]
		DataCols=[0,2,3,4,6,8]
		UnitCols=[1,5,7,9]
		self.Data = genfromtxt(FileName,skip_header=self.RowLimits[0], skip_footer=Footer,usecols=DataCols)
		self.Units = genfromtxt(FileName,skip_header=self.RowLimits[0], skip_footer=Footer,dtype='str',usecols=UnitCols)
		self.Energy = self.Data[:,0]
		for i in range(len(self.Energy)):
			if self.Units[i,0] == 'keV':
				self.Energy[i] = self.Energy[i] *1e3
			if self.Units[i,0] == 'MeV':
				self.Energy[i] = self.Energy[i] *1e6
			if self.Units[i,0] == 'GeV':
				self.Energy[i] = self.Energy[i] *1e9

		self.ElectronicStopping = self.Data[:,1]
		self.NuclearStopping = self.Data[:,2]
		self.Stopping = self.ElectronicStopping+self.NuclearStopping

		Data1 = self.Data[:,3:]
		Units1 = self.Units[:,1:]
		for i in range(len(Data1[:,0])):
			for j in range(len(Data1[0,:])):
				if Units1[i,j]=='A':
					Data1[i,j] = Data1[i,j]*1e-10
				if Units1[i,j]=='um':
					Data1[i,j] = Data1[i,j]*1e-6
				if Units1[i,j]=='mm':
					Data1[i,j] = Data1[i,j]*1e-3
				if Units1[i,j]=='cm':
					Data1[i,j] = Data1[i,j]*1e-2
				if Units1[i,j]=='m':
					Data1[i,j] = Data1[i,j]*1.0
		self.Range = Data1[:,0]
		self.LongitudinalStraggling = Data1[:,1]
		self.LateralStraggling = Data1[:,2]		

#Data = SRIMData()
