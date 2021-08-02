#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 00:34:23 2021

@author: vova
"""

from random import random

N = 20
a = [0] * N
for i in range(N):
   a[i] = int(random()*15)
   print(a[i],end=' ')
   
print()

for i in range(N):
    f = True
    for j in range(N):
        if a[i] == a[j] and i != j:
            f = False
            break
    if f == True:
        print(a[i],end=' ')
        
