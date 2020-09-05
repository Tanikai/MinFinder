from random import shuffle

# This module is used for generating a set of random numbers.

def GetUnsortedSet(i_count):
    numberSet = [i for i in range(1, i_count+1)]
    shuffle(numberSet)
    return numberSet

def GetSortedSet(i_count):
    numberSet = [i for i in range(1, i_count+1)]
    return numberSet

def GetReverseSortedSet(i_count):
    numberSet = [i for i in range(1, i_count+1)]
    numberSet.reverse()
    return numberSet