#!/usr/bin/env python3
#
# Author: Jonathan Heard
#
# Based on work in Python One-liners Chapter 1
#
# Python Refresher and self study
#

# Boolean data type

# 1. Boolean Operations
x, y = True, False



print("\n x = ", x)
print("\n y = ", y)
print("\n (x and not y):\t", (x and not y))  # True
print("\n (not x and y or x):\t", (not x and y or x))  # True

# 2. If condition evaluates to False
print("\nIf condition evaluates to False")
print("if None or 0 or 0.0 or '' or [] or {} or set():")

if None or 0 or 0.0 or '' or [] or {} or set():
    print("\nDead code")  # Not reached

print("\nCode reached due False if condition!")
