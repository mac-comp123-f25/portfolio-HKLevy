from my_sum import *

def test_sum3_ints():
    assert sum3([2,4,-6])==0

def test_sum3_floats():
    assert sum3([-0.1,0.5,0.6])==1
