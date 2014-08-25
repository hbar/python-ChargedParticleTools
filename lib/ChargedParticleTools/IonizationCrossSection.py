from numpy import *
import matplotlib.pyplot as pl

class IonizationCrossSection(object):
    def __init__ (self,element,Ei=1e4,shell='k',subshell=1):
        self.element = element
        self.shell = shell
        self.ionizationEnergy = Ei
        Z = element.z
        print self.shell
        if self.shell=='k' or self.shell=='K':
            An = 3.135e9 * Z**(-4.3434)
            Bn = exp(0.665 - 0.614 * log(Z) + 0.0810*(log(Z))**2 - 0.00005*(log(Z))**3 )
            self.label=self.element.symbol + '(K)'

        if ((shell=='l' or shell=='L') and subshell == 1) or shell=='L1':
            An = 2.203e12 * Z**(-5.109) 
            Bn = 12.909 * Z**(-1.006)
            self.label=self.element.symbol + r'(L$_1$)'

        if ((shell=='l' or shell=='L') and subshell == 2) or shell=='L2':
            An = 7.5231e12 * Z**(-5.3305) 
            Bn = exp(4.4243 - 2.0777 * log(Z) + 0.2039*(log(Z))**2 ) - 0.5
            self.label=self.element.symbol + r'(L$_2$)'

        if ((shell=='l' or shell=='L') and subshell == 3) or shell=='L3':
            An = 6.599e12 * Z**(-5.0797) 
            Bn = 4.8642* Z**(-0.5645) - 0.5
            self.label=self.element.symbol + r'(L$_3$)'

#        else:
 #           An = nan
  #          Bn = nan
   #         print 'Electron Shell Input Error'
        self.constantAn = An
        self.constantBn = Bn


    def crossSection(self,Energy):
        U = Energy/self.ionizationEnergy
        An = self.constantAn
        Bn = self.constantBn
        print An, Bn
        sigma = An/(Bn + U) * log(U)
        for i in range(len(U)):
            if sigma[i] < 0.0:
                sigma[i] = 0.0
        return sigma


    def plotU(self,U=linspace(1,5,100)):
        An = self.constantAn
        Bn = self.constantBn
        sigma = An/(Bn + U) * log(U)
        pl.semilogy(U,sigma)
#        pl.plot(U,sigma)
        pl.xlabel('U = E/Ei')
        pl.ylabel(r'cross section $\sigma(U)$ [barns]')

    def plotE(self,Energy=linspace(1,30e3,1000)):
        print Energy
        sigma=self.crossSection(Energy)
        print sigma
        pl.semilogy(Energy*1e-3,sigma,label=self.label)
        pl.xlabel('Energy [keV]')
        pl.ylabel(r'cross section $\sigma(U)$ [barns]')
