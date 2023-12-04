#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:38:46 2023

@author: Gaëtan LE FLOCH - gaetan[dot]lefloch[at]yahoo[dot]fr

Advent of calendar

Day 1
"""

import re

with open('list_of_inputs.txt') as f:
    data = f.readlines()
    
modified = []
for i in data:
    j = re.sub("[^0-9]", "",i)
    j = j[0] + j[-1]
    modified.append(j)
    
sum_el = 0
for i in modified:
    sum_el += int(i)
    
print(sum_el) # Here it is.
    
    
