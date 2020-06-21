# -*- coding: utf-8 -*-
"""
Hypersphere Radius: What value of radius would one need to maintain a hypersphere volume of 1 with increasing d.
Plot this value for d=1,⋯,100.
Author: Ravindra Neralla
"""

import matplotlib.pyplot as matplt
from scipy.special import gamma
from math import pi

# Calculate the radius using volume
radius_arr = []
# Defining dimension for the plot
d = [x for x in range(1, 101)]

# hypersphere dimension range is 1 to 100
for i in range(1, 101):
    # given volume is 1
    v = 1
    r = gamma((i / 2 + 1) ** 1 / i) / pi ** 0.5 * v ** 1 / i
    radius_arr.append(r)

print(radius_arr)

# Plotting
matplt.plot(d, radius_arr)
matplt.xlabel("d")
matplt.ylabel("Volume")
matplt.show()