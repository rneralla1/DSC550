# -*- coding: utf-8 -*-
"""
Hypersphere Volume: Plot the volume of a unit hypersphere as a function of dimension. Plot for d=1,⋯,50.
Author: Ravindra Neralla
"""


import matplotlib.pyplot as plt
from math import pi
from scipy.special import gamma

#Define list for volume
volume_arr=[]
#Define dimension for plot
d=[x for x in range(1,51)]

# calculate volumes of the hypersphere for range(1,50) dimensions
for i in range(1,51):
        #radius is 1 as it is unit radius
        r=1
        # volume formula
        vol=(pi**i/2/gamma(i/2+1))*r**i
        #append it to the volume list
        volume_arr.append(vol)

print(volume_arr)

# Plot using matplotlib
plt.plot(d,volume_arr)
plt.xlabel("d")
plt.ylabel("Volume")
plt.show()