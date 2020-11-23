"""misc_performance

This module contais miscellaneous functions that illustrate various performace
improvement techniques. The comparison of the performance is done using the
timeit module.
"""
import timeit
from collections import defaultdict
from collections import deque

# Change the sample size accordingly to your computer resources.
sample_size_1 = 500000
sample_size_2 = 1000

def no_list_comprehension_ex1():
    mylist = []
    for i in range(sample_size_1):
        mylist.append(i*i)

def list_comprehension_ex1():
    mylist = [i*i for i in range(sample_size_1)]

def no_list_comprehension_ex2():
    mylist = []
    for i in range(sample_size_2):
        for j in range(sample_size_2):
            mylist.append(i*j)

def list_comprehension_ex2():
    mylist = [i*j for i in range(sample_size_2) for j in range(sample_size_2)]

def no_dict_comprehension():
    d = {}
    for i in range(sample_size_1):
        d[i] = i*i

def dict_comprehension():
    d = {i: i*i for i in range(sample_size_1)}

def no_if_condition_loop_opt():
    num = 1000
    val = 0
    for i in range(sample_size_1):
        if num < 100:
            val += i*i
        else:
            val += i*i*i
    return val

def if_condition_loop_opt():
    num = 1000
    val = 0
    if num < 100:
        for i in range(sample_size_1):
            val += i*i
    else:
        for i in range(sample_size_1):
            val += i*i*i
    return val

def not_using_try():
    mylist = []
    val = 1
    for i in range(sample_size_1):
        if i == 0:
            val /= 10
        else:
            val /= i
        mylist.append(val)

def using_try():
    mylist = []
    val = 1
    for i in range(sample_size_1):
        try:
            val /= i
        except ZeroDivisionError:
            val /= 10
    mylist.append(val)

def data_struct_choice_list():
    mylist = [i*i for i in range(1000)]
    val = 0
    for j in range(100000):
        if j in mylist:
            val += j
        else:
            val += j*2

    print("val is: {0}".format(val))
    return val

def data_struct_choice_set():
    # Python 'set' comprehension just like a dict or list
    myset = {i*i for i in range(1000)}
    val = 0
    for j in range(100000):
        if j in myset:
            val += j
        else:
            val += j*2

    print("val is: {0}".format(val))
    return val

def dict_counter():
    unit_headcount = {}
    game_characters = ['elf', 'knight', 'orc', 'orc',
                       'knight', 'knight'] * sample_size_1

    # Loop over the list
    for unit in game_characters:

        # Count the occurance of each character and store
        # the result in the dictionary object unit_headcount
        if unit in unit_headcount:
            unit_headcount[unit] += 1
        else:
            unit_headcount[unit] = 1

    return unit_headcount

def defaultdict_counter():
    unit_headcount = defaultdict(int)
    game_characters = ['elf', 'knight', 'orc', 'orc',
                       'knight', 'knight'] * sample_size_1

    for unit in game_characters:
        unit_headcount[unit] += 1

    return unit_headcount

# Create the list and deque objects
lst = list(range(sample_size_1))
dq = deque(range(sample_size_1))

def list_example():
    for i in range(sample_size_1):
        lst.pop()

def deque_example():
    for i in range(sample_size_1):
        dq.pop()

def list_comprehension_sum():
    my_data = [i for i in range(sample_size_1)]
    sum(my_data)

def generator_expression_sum():
    my_data = (i for i in range(sample_size_1))
    sum(my_data)

def run_timeit(func_1, func_2, num=1):
    """Run timeit.timeit for the given function names (input args)"""
    t1 = timeit.timeit("{0}".format(func_1),
            setup="from __main__ import {0}".format(func_1), number=num)
    t2 = timeit.timeit("{0}".format(func_2),
            setup="from __main__ import {0}".format(func_2), number=num)

    print("Function: {func:<25}, time: {t}".format(func=func_1, t=t1))
    print("Function: {func:<25}, time: {t}".format(func=func_2, t=t2))
    print("~"*66)

if __name__ == '__main__':

    run_timeit("no_dict_comprehension", "dict_comprehension")
    run_timeit("list_example", "deque_example")
    run_timeit("dict_counter", "defaultdict_counter")
    run_timeit("data_struct_choice_list", "data_struct_choice_set")
    run_timeit("not_using_try", "using_try")
    run_timeit("no_if_condition_loop_opt", "if_condition_loop_opt")
    run_timeit("list_comprehension_sum", "generator_expression_sum")
