"""
Non Derivable Itemsest
Author: Ravindra Neralla
"""

import pandas as pd
from itertools import combinations


# creating function to pass arguments
def formCombinations(itemset, num):
    # creating list
    combArr = []
    # loop through itemset
    for comb in combinations(itemset, num):
        # appending in empty list
        combArr.append(comb)
    return combArr


# function to calculate the bound value
def calc_value(st, itemset, dictionary, n):
    # build subsets based on combinations
    value = 0.0
    for num in range(n - 1, 0, -1):
        # Get the subsets
        subsets = formCombinations(itemset, num)
        for comb in subsets:
            ck = all(item in comb for item in st)
            # i increments
            if ck or st == ():
                i = int(dictionary[comb]) * pow(-1.0, (n + 1) - num)
                value += i
    # check if the combination set is empty to update dict values
    if st == ():
        empty = 0
        for dict_value in dictionary.values():
            empty += int(dict_value)
        value += empty * pow(-1.0, (n + 1))
    return value


if __name__ == '__main__':
    # Read the two input files
    itemset_df = pd.read_csv('itemsets.txt', header=None)
    ndi_df = pd.read_csv('ndi.txt', header=None)

    # converting itemsets to dictionary
    itemset_dict = {}
    for i, itemset_support in enumerate(itemset_df[0]):
        set_support_list = []
        # splitting
        for val in itemset_support.split(' '):
            # passing hypen condition
            if val == '-':
                continue
            else:
                set_support_list.append(val)
        itemset_dict[tuple(set_support_list[:-1])] = set_support_list[-1]
    # ndi file datasets
    ndi_dict = {}
    for i, itemset in enumerate(ndi_df[0]):
        ndi_dict[i] = itemset.split(' ')
    for itemset in ndi_dict.values():
        upperList = []
        lowerList = []
        lower = 0
        upper = 0
        n = len(itemset)
        # breaking down combinations into subsets
        for ind in range(len(itemset)):
            subsets = formCombinations(itemset, ind)
            boolean_Odd = (n - len(subsets[0])) % 2
            for comb in subsets:
                if boolean_Odd:
                    upperList.append(calc_value(comb, itemset, itemset_dict, n))
                else:
                    lowerList.append(calc_value(comb, itemset, itemset_dict, n))
        # Upper bound
        upper = min(upperList)
        # lower bound code
        if max(lowerList) < 0:
            lower = 0
        else:
            lower = max(lowerList)
        # Check if it is derivable
        if lower == upper:
            ans = '-->Derivable'
        else:
            ans = '-->Non-Derivable'
        print('{}: [{}, {}] {}'.format(itemset, lower, upper, ans))