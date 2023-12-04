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
sum_el = 0
for i in data:
    j = re.sub("[^0-9]", "",i)
    sum_el += int(j[0] + j[-1]) # First and last digits
    
print(sum_el) # Here it is.
    
    
