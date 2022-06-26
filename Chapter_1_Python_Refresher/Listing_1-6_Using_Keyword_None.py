#!/usr/bin/env python3
#
# Author: Jonathan Heard
#
# Based on work in Python One-liners Chapter 1
#
# Python Refresher and self study
#

# String data types and common String Methods

# Most Important String Methods

y = "    This is lazy \t\n   "
print("\ny = ", y)

print("print(y.strip()")
print(y.strip())
# Remove Whitespace: 'This is lazy'

print("\n(print('DrDre'.lower())")
print("DrDre".lower())
# Lowercase: 'drdre'

print('\nprint("smartphone".startswith("smart"))')
print("smartphone".startswith("smart"))
# Matches the string's prefix against the argument: True

print('\nprint("smartphone".endswith("phone"))')
print("smartphone".endswith("phone"))
# Matches the string's suffix against the argument: True

print('\nprint("another".find("other"))')
print("another".find("other"))
# Match index: 2

print('\nprint("cheat".replace("ch", "m"))')
print("cheat".replace("ch", "m"))
# Replace all occurrences of the first argument with the second argument: meat

print('\nprint(".".join(["F", "B", "I", " "]))')
print(".".join(["F", "B", "I", " "]))
# Glues together all elements in the list using the seperator string: F.B.I.

print('\nprint(len("Rumpelstiltskin"))')
print(len("Rumpelstiltskin"))
# String length: 15

print('\nprint("ear" in "earth")')
print("ear" in "earth")
# Contains: True


