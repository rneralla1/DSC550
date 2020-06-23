"""
Diagonals of High dimensions
Author: Ravindra Neralla
"""

import numpy as np
import math
import matplotlib.pyplot as pyplt
from scipy import stats
from collections import Counter


# creating class counter for PMF calculation.
class calc_PMF(Counter):
    # normalizing pmf to add probabalities by 1
    def Normalize_pmf(self):
        sum_ = float(sum(self.values()))
        for key in self:
            self[key] /= sum_


# applying formula to calculate angle
def calc_angle(point1, point2):
    return np.dot(point1, point2) / (np.linalg.norm(point1) * np.linalg.norm(point2))


# Function to get the array of angles for d-dimensions
def calc_angle_in_d(n, d):
    results = np.zeros(n)
    i = 0
    while (i < n):
        points_pre = np.random.rand(2, d)
        points_pre[points_pre <= 0.5] = -1
        points_pre[points_pre > 0.5] = 1
        cos_theta = calc_angle(points_pre[0], points_pre[1])
        results[i] = round(math.degrees(math.acos(cos_theta)), 2)
        i = i + 1
    return results


# Plot using matplot
def plot_matplot(pr):
    pyplt.hist(pr, bins=20)
    pyplt.xlabel('Size')
    pyplt.ylabel('EPMF')
    pyplt.show()


# creating function for plot
def plot(angle):
    p = calc_PMF(angle)
    p.Normalize_pmf()
    keyList = []
    probList = []
    for key, prob in p.items():
        keyList.append(key)
        probList.append(prob)
    plot_matplot(probList)


if __name__ == '__main__':
    n = 100000
    # LIst for d values
    d_arr = [10, 100, 1000]

    for d in d_arr:
        angle = calc_angle_in_d(n, d)
        plot(angle)
        print('Angle Description for d = 10 :\n', stats.describe(angle), '\n')

    print('The angle becomes 90 degree when the dimension is increased.'
          'In high dimensions, the digonal vectors are perpendicular the co-ordinate axes'
          ' with 2**d corners in d-dimensional hypercubes and 2**d diagonal vectors from the origin to all corners.')