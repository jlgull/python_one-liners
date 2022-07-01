#!/usr/bin/env python3
#
# Author: Jonathan Heard
#
# Based on work in Python One-liners Chapter 1
#
# Python Refresher and self study
#

# The Keyword is, check whether 2 variables refer to the same object in memory.

print("\ny = x = 3")
y = x = 3

print("\nprint(x is y)")
print("Result is 'True'")
print(x is y)

print("\nprint([3] is [3])")
print("Result is 'False'")
print([3] is [3])
