# -*- coding: utf-8 -*-
"""
Exercise 3.1.1: Compute the Jaccard similarities of each pair of the following three
sets: {1,2,3,4}, {2,3,5,7}, and {2,4,6}.
Author: Ravindra Neralla
"""

A = {1, 2, 3, 4}
B = {2, 3, 5, 7}
C = {2, 4, 6}


def Jaccard(set1, set2):
    s1 = set(set1)
    s2 = set(set2)
    return len(s1.intersection(s2)) / len(s1.union(s2))


# defining main function to called jaccard similarities
def main():
    print("The jaccard similarity between B and C:", Jaccard(B, C))
    print("The jaccard similarity between B and A:", Jaccard(B, A))
    print("The jaccard similarity between C and A:", Jaccard(C, A))
    # Percentage values
    print("The percentage of jaccard similarity between B and C:", Jaccard(B, C) * 100)
    print("The percentage of jaccard similarity between B and A:", Jaccard(B, A) * 100)
    print("The percentage of jaccard similarity between C and A:", Jaccard(C, A) * 100)


if __name__ == '__main__':
    main()