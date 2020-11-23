"""compare_memory

This module can be used by the memory_profiler to get line by line
memory consumption output for the given functions.

Run this program as follows:

    $ python -m memory_profiler compare_memory.py
"""
from itertools import chain

def get_data():
    for i in range(3):
        yield i

@profile
def list_comp_memory():
    sample_size = 10000
    my_data = [i for i in range(sample_size)]

@profile
def generator_expr_memory():
    sample_size = 10000
    my_data = (i for i in range(sample_size))

# Create some lists that will be 'chained' together
data_1 = ['x'] * 10000
data_2 = ['y'] * 10000
data_3 = ['z'] * 10000

@profile
def chain_memory():
    mychain = chain(data_1, data_2, data_3)
    for i in mychain:
        pass
@profile
def list_memory():
    mylist = data_1 + data_2 + data_3
    for i in mylist:
        pass

if __name__ == '__main__':
    list_comp_memory()
    generator_expr_memory()
    chain_memory()
    list_memory()
