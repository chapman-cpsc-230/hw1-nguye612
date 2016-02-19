"""
File: <sin2_plus_cos2.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<I debugged the given codes from the book.>
"""


#Part A
from math import sin, cos
pi = 3.14159265359
x = pi/4.0
y = sin(x)**2 + cos(x)**2
print y


#Part B
v0 = 3.0 #m/s
t = 1.0 #s
a = 2.0 #m/s**2
s = v0*t + 0.5*a*t**2
print s, "meters"


#Part C
a = 3.3
b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a+b)**2
eq2_pow = (a-b)**2


print "first equation %g = %g" %(eq1_sum, eq1_pow)
print "second equation %g = %g" %(eq2_sum, eq2_pow)
