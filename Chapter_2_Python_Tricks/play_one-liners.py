#!/usr/bin/env python3
#
# Author: Jonathan Heard
#
# Based on work in Python One-liners Chapter 2
#
# List compression examples and self study
#

"""
print([x  x in range(5)])
# [0, 1, 2, 3, 4]
"""

print([x for x in range(5)])

# Data
employees = {'Alice': 100000,
             'Bob': 99817,
             'Carol': 122908,
             'Frank': 88123,
             'Eve': 93121}

# One-Liner

top_earners = [(name, salary) for name, salary in employees.items() if salary >= 100000]

# Result
print(top_earners)

# Personal use of List compression.

f_two_c = [(deg_F, (deg_F - 32) * 5 / 9) for deg_F in range(32, 215, 45)]

print(f_two_c)
