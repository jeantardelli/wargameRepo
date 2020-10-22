import random

def weighted_random_selection(obj1, obj2):
    """Randomly select between two objects based on assigned 'weight'"""
    selection = random.choices([id(obj1), id(obj2)], weights=[0.3, 0.7])
    if selection[0] == id(obj1):
        return obj1
    return obj2

def print_bold(msg, end='\n'):
    """Print a desired messsage in bold"""
    print("\033[1m" + msg + "\033[0m", end=end)

