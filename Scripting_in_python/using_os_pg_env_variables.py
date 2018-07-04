"""
    1. Prints the first ten digits of PI to the screen.
    2. Accepts an optional environment variable called DIGITS. 
    If present, the script will print that many digits of PI 
    instead of 10.
"""

from os import getenv
from math import pi

digits = int(getenv("DIGITS") or 10)
print("%.*f" % (digits, pi))
