import sys
sys.path.append('../lib/')
from ChargedParticleTools import *
from numpy import *
import pylab as pl


Energy = logspace(0,10,1000)
H = Element('H')
Mo = Element('Mo')

SMo  = IonStoppingCrossSection(target=Mo,ion=H)

SigmaEMo = SMo.sigmaE(Energy)

pl.figure()
pl.loglog(Energy,SigmaEMo)

# pl.figure()
# SigmaMoK.plotE();
# SigmaMoL1.plotE();
# SigmaMoL2.plotE();
# SigmaMoL3.plotE();
# pl.legend(loc=4)
# pl.title('Electron Impact Ionization Cross Section')

pl.show()
