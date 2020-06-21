# -*- coding: utf-8 -*-
"""
Exercise 3.4.1: Evaluate the S-curve 1−(1−sr)b for s = 0.1,0.2,...,0.9,
for the following values of r and b: • r = 3 and b = 10. • r = 6 and b = 20. • r = 5 and b = 50.
Author: Ravindra Neralla
"""

import matplotlib.pyplot as matplt
r1 = 3
b1 = 10
r2 = 6
b2 = 20
r3 = 5
b3 = 50
s_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
def curve_readings(a, b):
    s = []
    length=len(s_values)
    for i in range(0,length):
        s.append(1-(1-s_values[i]**a)**b)
    return s
def plot_curve(list_values):
    matplt.title("S_Value Vs S_Curve Plot")
    x=s_values
    y=list_values
    matplt.plot(x,y)
    matplt.xlabel('S Values')
    matplt.ylabel("S Curve Values")
if __name__ == '__main__':
    curve1=curve_readings(r1,b1)
    curve2=curve_readings(r2,b2)
    curve3=curve_readings(r3,b3)
    # Plotting three curves
    plot_curve(curve1)
    plot_curve(curve2)
    plot_curve(curve3)