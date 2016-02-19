"""
File: <interest_rate.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Determining the growth of 1000 euros in a bank after 3 years at a five percent interest rate.>
"""

A = 1000.0
p = 0.05
n = 3
FV = A*(1+p) ** n

print "After three years, the value is", FV, "euros."
