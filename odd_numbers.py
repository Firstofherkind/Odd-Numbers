# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:47:17 2021

@author: JENI
"""

def odd(x):
    odd = []
    for i in range (x):
        if i % 2 != 0:
            odd.append(i)
            
    return odd


print(odd(10))