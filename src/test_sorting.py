from Sorting import *

def test_merge():
    mylist = [10,9,8,7,10,15,2,13,1,15]
    result = [1,2,7,8,9,10,10,13,15,15]
    assert merge(mylist) == result
