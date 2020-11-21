"""profile_ex

This module contains supporting code to be used by cProfile. The cProfile can
be run on this file (from the commandline) as:

    $ python -m cProfile profile_ex.py
"""

def test_1():
    """Trivial multiplication example"""
    return 100 * 100

def test_2():
    """Trivial for looping example"""
    x = []
    for i in range(10000):
        temp = 1/1000.0
        x.append(temp*temp)
    return x

def test_3(condition=False):
    """Trivial recursion example"""
    if condition:
        test_3()

if __name__ == '__main__':
    a = test_1()
    b = test_2()
    c = test_3(True)
