#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:27:06 2016

@author: adaico
"""

import numpy as np
from numpy import linalg as la

a = np.array(np.random.normal(0, 1, (5, 5)))
val, vect = la.eig(a)
for i in range(5):
    print(np.array_equal(np.round(np.dot(a, vect[:,i]), 5), np.round((val[i] * vect[:,i]), 5)))
    


