from random import shuffle

# This module is used for generating a set of random numbers.

def GetUnsortedSet(i_count):
    List = [i for i in range(1, i_count+1)]
    shuffle(List)
    return List
