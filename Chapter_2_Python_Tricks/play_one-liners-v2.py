#!/usr/bin/env python3
#
# Author: Jonathan Heard
#
# Based on work in Python One-liners Chapter 2
#
# List compression examples and self study
#

# Data
text = "Call me Ishmael. Some years ago - never mind how long precisely - having " \
       "little or no money in my purse, and nothing particular to interest me "\
       "on shore, I thought I would sail about a little and see the watery part " \
       "of the world. It is a way I have of driving off the spleen, and regulating " \
       "the circulation.  - Moby Dick"

# One-Liner
text_line = str(text.split('\n'))
print(f"What type is text_line", type(text_line), "\n", text_line, "\n")

w = [[x for x in line.split() if len(x) > 3]for line in text.split('\n')]

print(type(w))

# Result
print(w)
