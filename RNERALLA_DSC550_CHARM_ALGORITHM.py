# -*- coding: utf-8 -*-
"""
Implement CHARM algorithm for mushroom.txt file with minimum support 3000 and 5000
Author: Ravindra Neralla
"""

import pandas as pd


# Function to create CharmAlgorithm for the given minimum support value
def CharmAlgorithm(minsup_value):
    print("Filename:", 'mushroom.txt')
    print("Minsup:", minsup_value)
    items_list = []
    for columns_value in database.columns:
        support = database[columns_value].sum()
        if support >= minsup_value:
            items_list.append(int(columns_value))
        else:
            continue
    total = len(items_list)
    print('%d items have frequency greater than or equal to given minsup:' % total)
    print(items_list)


if __name__ == '__main__':
    f = open('mushroom.txt', 'r')
    dict_itemset = {}
    for tids, line_items in enumerate(f):
        dict_itemset[tids] = [j for j in line_items.split(' ')
                              if j != '\n']

    database = pd.Series(dict_itemset).str.join('|').str.get_dummies()
    try:
        CharmAlgorithm(3000)
        CharmAlgorithm(5000)
    except:
        print('You need both a filename and a minimum support value!')


