#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:08:38 2016

@author: adaico
"""

import numpy as np
import time as t

"""1"""
start = t.time()
np.linspace(-5, 6, 1100)
print(t.time() - start)


"""2"""
def cycle(s, e, n):
    array = []
    d = (e - s) / (n - 1)
    for i in range(n):
        array.append(s + i * d)
    return array

start = t.time()
cycle(-5, 6, 1100)
print(t.time() - start)


"""3"""
def list_comprehension(s, e, n):
    array = [s + (e - s) * i / (n - 1) for i in range(n)]
    return array

start = t.time()
list_comprehension(-5, 6, 1100)
print(t.time() - start)