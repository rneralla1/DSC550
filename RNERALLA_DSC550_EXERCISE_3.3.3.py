# -*- coding: utf-8 -*-
"""
(a) Compute the minhash signature for each column if we use the following three hash functions:
h1(x) = 2x + 1 mod 6; h2(x) = 3x + 2 mod 6; h3(x) = 5x + 2 mod 6.
(b) Which of these hash functions are true permutations?
(c) How close are the estimated Jaccardsimilarities for the six pairs of columns to the true Jaccard similarities?
Author: Ravindra Neralla
"""

import sys

# Given Data
elements = [0, 1, 2, 3, 4, 5]
s1 = (0, 0, 1, 0, 0, 1)
s2 = (1, 1, 0, 0, 0, 0)
s3 = (0, 0, 0, 1, 1, 0)
s4 = (1, 0, 1, 0, 1, 0)


def hash1(a):
    return ((2 * a) + 1) % 6


def hash2(a):
    return ((3 * a) + 2) % 6


def hash3(a):
    return ((5 * a) + 2) % 6


def hash_1(elements):
    hash_list = []
    for i in elements:
        hash_list.append(hash1(i))
    return hash_list


def hash_2(elements):
    hash_list = []
    for i in elements:
        hash_list.append(hash2(i))
    return hash_list


def hash_3(elements):
    hash_list = []
    for i in elements:
        hash_list.append(hash3(i))
    return hash_list


def compareNameAndList(hash_list_name, hash_list):
    hash_list.sort()
    elements.sort()
    if hash_list == elements:
        print(hash_list_name + ' is a true permutation of elements list')
    else:
        print(hash_list_name + ' is not a true permutation of elements list')


# Compute Jaccard similarity of two lists
def jaccard_similarity(a, b):
    # Intersection of two lists
    inter = len(list(set(a).intersection(b)))
    # Union of two lists
    union = (len(a) + len(b)) - intersection_cardinality(a, b)
    # compute Cardinality
    return round(float(inter) / union, 3)


# function to reverse columns and rows within the ss, filling a single list
def Rdata():
    hold_matrix = []
    for i in range(0, len(s1)):
        hold_matrix.append([s1[i], s2[i], s3[i], s4[i]])
    return hold_matrix


# function to compute intersection of two lists
def intersection_cardinality(a, b):
    return len(list(set(a).intersection(b)))


# function to compute union of two lists
def union_cardinality(a, b):
    return (len(a) + len(b)) - intersection_cardinality(a, b)


# Minhash signature code
def minhash(data, hashfuncs):
    rows = len(data)
    cols = len(data[0])
    sigrows = len(hashfuncs)
    sigmatrix = []
    for i in range(sigrows):
        sigmatrix.append([sys.maxsize] * cols)
    for r in range(rows):
        hashvalue = list(map(lambda a: a(r), hashfuncs))
        # if data != 0 and signature > hash value, replace signature with hash value
        for c in range(cols):
            if data[r][c] == 0:
                continue
            for i in range(sigrows):
                # if the sigmatrix value is greater than the hashvalue, replace with hashvalue
                if sigmatrix[i][c] > hashvalue[i]:
                    sigmatrix[i][c] = hashvalue[i]
    return sigmatrix


if __name__ == '__main__':
    # Calculate hash functions
    hashlist1 = hash_1(elements)
    hashlist2 = hash_2(elements)
    hashlist3 = hash_3(elements)
    # printing each values
    print('\nFirst hash list: ' + str(hash_1(elements)))
    print('Second hash list: ' + str(hash_2(elements)))
    print('Third hash list: ' + str(hash_3(elements)))

    # Compute minhash signature values
    print('\n(1) Compute the minhash signature for each column using three hash functions.')
    minhash_sig = minhash(Rdata(), [hash1, hash2, hash3])
    print('\n Minhash Signature Values: \n' + str(minhash_sig))

    # Compare to check if they are true permutations
    print('\n(2) Which of these hash functions are true permutations?')
    compareNameAndList('\nHash 1', hashlist1)
    compareNameAndList('Hash 2', hashlist2)
    compareNameAndList('Hash 3', hashlist3)

    # comparing estimated Jaccard similarities
    # Third questions
    print('\n(3) How close are the estimated Jaccard Similarities to the true Jaccard Similarities?')
    # similarities of 6 pairs of columns
    print('\nColumn 1 and Column 2:', str(jaccard_similarity(s1, s2)))
    print('Column 1 and Column 3:', str(jaccard_similarity(s1, s3)))
    print('Column 1 and Column 4:', str(jaccard_similarity(s1, s4)))
    print('Column 2 and Column 3:', str(jaccard_similarity(s2, s3)))
    print('Column 2 and Column 4:', str(jaccard_similarity(s2, s4)))
    print('Column 3 and Column 4:', str(jaccard_similarity(s3, s4)))

    # similarities of signatures
    # establish columns of signatures
    minhash_1 = [minhash_sig[0][0], minhash_sig[1][0], minhash_sig[2][0]]
    minhash_2 = [minhash_sig[0][1], minhash_sig[1][1], minhash_sig[2][1]]
    minhash_3 = [minhash_sig[0][2], minhash_sig[1][2], minhash_sig[2][2]]
    minhash_4 = [minhash_sig[0][3], minhash_sig[1][3], minhash_sig[2][3]]

    # similarities of signatures 1 & 2, 1 & 3, 1 & 4, 2 & 3, 2 & 4, 3 & 4
    print('\nSig 1 and Sig 2: ', str(jaccard_similarity(minhash_1, minhash_2)))
    print('Sig 1 and Sig 3: ', str(jaccard_similarity(minhash_1, minhash_3)))
    print('Sig 1 and Sig 4: ', str(jaccard_similarity(minhash_1, minhash_4)))
    print('Sig 2 and Sig 3: ', str(jaccard_similarity(minhash_2, minhash_3)))
    print('Sig 2 and Sig 3: ', str(jaccard_similarity(minhash_2, minhash_4)))
    print('Sig 3 and Sig 4: ', str(jaccard_similarity(minhash_3, minhash_4)))

    print('\nThe estimated Jaccard similarities are not close to the true Jaccard similarities.')