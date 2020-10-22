import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

# optionally print the sys.path for debugging
print("in __init__.py sys.path:\n {0:s}".format(':'.join(sys.path)))


