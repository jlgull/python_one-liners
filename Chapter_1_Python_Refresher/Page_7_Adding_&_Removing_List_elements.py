#!/usr/bin/env python3
#
# Author: Jonathan Heard
#
# Based on work in Python One-liners Chapter 1
#
# Python Refresher and self study
#

# 3 Methods to add elements to an existing list

# 1. Append
print("\nMethod 1, Append")

print("l = [1, 2, 2]")
l = [1, 2, 2]

print("l.append(4)")
l.append(4)

print("print(l)")
print("Result: [1, 2, 2, 4]")
print(l)

# 2. Insert
print("\nMethod 2, Insert")

print("l = [1, 2, 4]")
l = [1, 2, 4]

print("l.insert(2, 3)")
l.insert(2, 2)

print("print(l)")
print("Result: [1, 2, 2, 4]")
print(l)

# 3. List Concatenation
print("\nMethod 3, List Concatenation")

print("print([1, 2, 2] + [4])")
print("Result: [1, 2, 2, 4]")
print([1, 2, 2] + [4])


# Removing a list item

print("\nl = [1, 2, 2, 4]")
l = [1, 2, 2, 4]

print("l.remove(1)")
l.remove(1)

print("print(l)")
print("Result: [2, 2, 4]")
print(l)