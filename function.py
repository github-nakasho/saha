
"""===============================================================

function.py 

purpose: define function



2018 Jan. 03: coded by Sho K. NAKAMURA

==============================================================="""


import constant
import numpy
import math


### define function ###

def function(rho, t):

	ft=((constant.mp/rho)
		*(2.0*math.pi*constant.me*constant.kb*t/constant.h**2)**(1.5)
		*numpy.exp(-constant.chi/(constant.kb*t)))


	return ft

