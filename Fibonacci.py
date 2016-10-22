#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 00:08:05 2016

@author: adaico
"""
a = 0
b = 1
for i in range(100 - 2):
    c = a
    a = b
    b += c 
print(b)