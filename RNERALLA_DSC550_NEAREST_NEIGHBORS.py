# -*- coding: utf-8 -*-
"""
Nearest Neighbors: Assume we have a unit hypercube centered at (0.5,⋯,0.5). Generate n=10000 uniformly random points
in d dimensions, in the range (0,1) in each dimension. Find the ratio of the nearest and farthest point from the center of the space. Also store the actual distance of the nearest dn and farthest df points from the center. Plot these value for d=1,⋯,100.
Author: Ravindra Neralla
"""

import random
import matplotlib.pyplot as matplt


# Function to create 100 x 10000 random uniform matrix
def neighbors(d):
    arr = []
    for x in range(len(d)):
        uniform = []
        for n in range(10000):
            uniform.append(random.uniform(0, 1))
        arr.append(uniform)
    return arr


# Function to get closest number from 0.5 in the list
def close(list, k=0.5):
    return list[min(range(len(list)), key=lambda i: abs(list[i] - k))]


# Function to get farthest number from 0.5 in the list
def farth(list, k=0.5):
    return list[max(range(len(list)), key=lambda i: abs(list[i] - k))]


if __name__ == '__main__':
    try:
        # Set dimensions-range(1,100)
        d = [x for x in range(1, 100)]

        hypercube = neighbors(d)

        # near, far = get_nearest_neighbors(hypercube)
        near = []
        far = []
        for i in range(len(hypercube)):
            # Insert with absolute difference value from closest point
            near.append(abs(0.5 - close(hypercube[i])))
            # Insert with absolute difference value from farthest point
            far.append(abs(0.5 - farth(hypercube[i])))

            # Plot closest distances for each d
        matplt.title('Closest point Distance VS d')
        matplt.plot(d, near)
        matplt.xlabel('Dimension - d')
        matplt.ylabel('Nearest distance')
        matplt.show()

        # Plot farthest distances for each d
        matplt.title('Farthest point Distance VS d')
        matplt.plot(d, far)
        matplt.xlabel('Dimension - d')
        matplt.ylabel('Farthest distance')
        matplt.show()

    except Exception as exception:
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));
    finally:
        print("Implemented the plot successfully.")
