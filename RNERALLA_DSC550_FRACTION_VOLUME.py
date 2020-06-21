# -*- coding: utf-8 -*-
"""
Fraction of Volume: Assume we have a hypercube of edge length l=2 centered at the origin (0,0,⋯,0). Generate n=10,000 points uniformly at random for increasing dimensionality d=1,⋯,100.
Author: Ravindra Neralla
"""

import matplotlib.pyplot as matplt
from scipy.special import gamma
from math import pi

if __name__ == '__main__':

    # Define variables to store two plot values
    fractions = []
    fractions_thinsphere = []
    # Define dimensions for two plots
    d = [x for x in range(1, 100)]
    dimensions = [x for x in range(1, 400)]
    try:
        # Calculate volumes
        for i in d:
            volume = (pi ** i / 2) / gamma(i / 2 + 1)
            fractions.append(volume)
        # Plot for fractions
        matplt.plot(d, fractions)
        matplt.xlabel("d")
        matplt.ylabel("Fraction Of point")
        matplt.show()
        # Calculate volumes for thin sphere
        for i in dimensions:
            l = 2
            e = 0.01
            r = l / 2
            # with the higher dimention it goes to 1
            volume = 1 - (1 - e / r) ** i
            fractions_thinsphere.append(volume)
            # Plots for fractions of thin sphere
        matplt.plot(dimensions, fractions_thinsphere)
        matplt.xlabel("dim")
        matplt.ylabel("Fraction Of point for thin shell")
        matplt.show()
    except Exception as exception:
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));
    finally:
        print("Implemented both the plots succesfully.")