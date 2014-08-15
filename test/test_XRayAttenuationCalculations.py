import sys
sys.path.append('../lib/')
from ChargedParticleTools import *
from numpy import *
import pylab as pl

RhoMo = 10.28
RhoB = 2.46
RhoW = 19.25

MoL = 2625.98 # [2867.20, 2625.98, 2521.1] 
MoK = 20000.5

XB  = Attenuation(Z=5)
XMo = Attenuation(Z=42)
XW  = Attenuation(Z=74)

pl.figure()
XB.PlotAttenuation()
XMo.PlotAttenuation()
XW.PlotAttenuation()
pl.legend()


pl.figure();
XB.MeanFreePath(Rho=RhoB)
XMo.MeanFreePath(Rho=RhoMo)
XW.MeanFreePath(Rho=RhoW)
pl.xlim(0,50e3)
pl.legend()

pl.figure(); 
#XMo.Intensity(PhotonE=3e3,Rho=RhoMo)
#XMo.Intensity(PhotonE=16e3,Rho=RhoMo) 
dX,I1=XMo.Intensity(PhotonE=MoL,Rho=RhoMo)
dX,I2=XMo.Intensity(PhotonE=MoK,Rho=RhoMo)
pl.semilogx(dX,I1/I2)

pl.figure(); 
dX,I1=XB.Intensity(PhotonE=MoL,Rho=RhoB)
dX,I2=XB.Intensity(PhotonE=MoK,Rho=RhoB)

pl.figure()
pl.semilogx(dX,I1)
pl.show()
