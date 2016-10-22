#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 03:50:34 2016

@author: adaico
"""
array1 = [1, 2, 7, 4, 5, 0, 61, 2, 0, 5, 21, 8, 37, 49, 0, 8, 9, 8, 27, 0, 9, 29, 12, 9, 28, 9, 38, 70, 8, 9, 64]
array2 = [10, 4, 6, 6, 20, 10, 3, 7, 10]


def qsort(array): 
    if len(array) in [0,  1]: 
        return array 
    else: 
        return qsort([x for x in array[1 : ] if x<array[0]]) + [array[0]] + qsort([x for x in array[1 : ] if x>=array[0]]) 
    
print(qsort(array1))
    