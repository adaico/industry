#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:35:30 2016

@author: adaico
"""

import matplotlib.pyplot as plt
import numpy as np

fig, sp = plt.subplots(nrows = 1, ncols = 2)

x = np.linspace(-10, 10, 1000)

sp[0].plot(x, x ** 3, label = 'cubic parabola')
sp[0].plot(x, np.sin(x) * 500, label = 'sin')
sp[0].plot(np.linspace(0, 10, 500), np.log(np.linspace(0.01, 10, 500)) * 500, label = 'log')
sp[0].axis([-10, 10, -1000, 1000])

sp[1].plot(x, x ** 2, label = 'parabola')
sp[1].plot(x, np.arctan(x) * 50, label = 'tg')
sp[1].axis([-10, 10, -100, 100])

for spi in sp:
    spi.set_xlabel('x axis')
    spi.set_ylabel('y axis')
    spi.grid(True) 
    spi.legend(loc = 2)
    
fig.savefig('plots.png', format = 'png')