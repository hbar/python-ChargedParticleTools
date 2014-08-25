## Implementation of the bethe bloch equation to calculate stopping power for ions

from numpy import *
from constants import *


class IonStopping(energy,element,ion,density) 

	C1=[]; C2=[]; C3=[]

	gamma = 1.0 + energy/ion.m0
	beta = sqrt(1.0-1.0/gamma**2)

	for i in range(len(element)):
		Zt = element[i].z

		C1.append( ((q0**2)/(4.0*pi*ep0))**2 )

		C2.apped( (4.0 * pi * zIon**2 * density[i] * Zt * rho)/(Me * A) )

		C3.append( 2.0 * me * beta**2 / (element[i].ionization * (1.0-beta) ) )
	
		dEdX = dEdZ + C1[i] * C2[i] * beta**-2 * ( log(C3[i] * beta**2) - beta**2 )

	return dEdX
