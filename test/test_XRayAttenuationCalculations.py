import sys
sys.path.append('../lib/')
from ChargedParticleTools import *
from numpy import *
import pylab as pl

RhoMo = 10.28
RhoB = 2.46

XMo = Attenuation(Z=42)
XB  = Attenuation(Z=5)

pl.figure()
XMo.PlotAttenuation()
XB.PlotAttenuation()


pl.figure();
XMo.MeanFreePath(Rho=RhoMo)
XB.MeanFreePath(Rho=RhoB)
pl.xlim(0,50e3)

pl.figure(); XMo.Intensity()
pl.show()
