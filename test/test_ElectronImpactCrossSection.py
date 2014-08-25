import sys
sys.path.append('../lib/')
from ChargedParticleTools import *
from numpy import *
import pylab as pl

RhoMo = 10.28
RhoB = 2.46
RhoW = 19.25

MoL = 2625.98 # 
MoL3 = 2867.20
MoL2 = 2625.98
MoL1 = 2521.1
MoK = 20000.5

AgL = 3432.3

Mo = Element('Mo')

# IonizationCrossSection((self,element,Ei=1e4,shell='k',subshell=1)
SigmaMoK  = IonizationCrossSection(element=Mo,Ei=MoK,shell='k')#,Ei=MoK,shell='k')
SigmaMoL1 = IonizationCrossSection(element=Mo,Ei=MoL1,shell='L1')
SigmaMoL2 = IonizationCrossSection(element=Mo,Ei=MoL2,shell='L2')
SigmaMoL3 = IonizationCrossSection(element=Mo,Ei=MoL3,shell='L3')

# pl.figure()
# pl.subplot(2,2,1); SigmaMoK.plotU(); pl.title('K')
# pl.subplot(2,2,2); SigmaMoL1.plotU(); pl.title('L1')
# pl.subplot(2,2,3); SigmaMoL2.plotU(); pl.title('L2')
# pl.subplot(2,2,4); SigmaMoL3.plotU(); pl.title('L3')

pl.figure()
SigmaMoK.plotE();
SigmaMoL1.plotE();
SigmaMoL2.plotE();
SigmaMoL3.plotE();
pl.legend(loc=4)
pl.title('Electron Impact Ionization Cross Section')

pl.show()
