from Sorting import *

l1 = [10,9,8,7,10,15,2,13,1,15]
r1 = [1,2,7,8,9,10,10,13,15,15]

def test_merge():
    assert merge(l1) == r1

def test_bubble():
    assert bubble(l1) == r1

def test_select():
    assert select(l1) == r1

def test_count():
    assert count(l1) == r1
