
"""===============================================================

main.py 

purpose: plot fraction of Hydrogen atom



2018 Jan. 03: coded by Sho K. NAKAMURA

==============================================================="""


### import some libraries ###

import numpy
from matplotlib import pyplot


### import .py files ###

import constant
import function


### input rho, T -> output ft & x=NII/Ntot ###

rho=1.0e-9
T=numpy.arange(5000, 25000)


ft=function.function(rho, T)
x=(-ft+numpy.sqrt(ft**2+4*ft))*0.5


### show result ###

pyplot.plot(T, x)
pyplot.show()

