#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 23:17:25 2021

"""

# посчитать все 2 в последовательности от 0 до n

n = int(input('input n '))

#0 1234567891011121314151617 18 19 20 21 22 23 24 25 222

c = 0

l = list(range(1, n+1))

for el in l:
    if '2' in  str(el):
        for two in str(el):
            if '2' == two:
                c += 1
        
cc = str(l).count('2') 
       
print(c, type(l), '\n', cc, type(cc))

# собрать все, потом в стринг, потом str.count(2),
# я без count написал-> c+=1 потому что count сначала не работал )
