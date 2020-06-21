# -*- coding: utf-8 -*-
"""
Exercise 3.2.1: What are the ﬁrst ten 3-shingles in the ﬁrst sentence of Section 3.2?

@Author: Ravindra Neralla
"""

givenStatement = 'The most effective way to represent documents as sets, for the purpose of identifying lexically similar documents is to construct from the document the set of short strings that appear within it.'
k = 3


def main():
    print('Given sentence == ', givenStatement, '\n')
    breakStatement = givenStatement.replace(',', '').split()
    print("First ten 3-shingles will be- ")
    for i in range(0, 10):
        print(str([breakStatement[i:i + k]]))


if __name__ == '__main__':
    main()