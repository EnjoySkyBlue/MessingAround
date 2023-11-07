
"""

Using an __init__.py file tells python that this directory is a package.
This will allow you to import modules (.py files) using import statements

V project 
    > package1
    > package2
    V package3
        > pymodule1.py
        > pymodule2.py
    > main.py

(in main.py)

from package3 import pymodule1 
from package2 import *


"""

# in the __init__ file, all this code is ran first and once when the package is loaded in.

print("Hello from the init file!")