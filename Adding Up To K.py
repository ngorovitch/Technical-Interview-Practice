# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:55:33 2018

@author: ngoro
"""

'''
Daily coding problem 

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
import util
import math 

from . import util

arr = [10, 15, 3, 8]
k = 17

#the simple way
for i in arr: 
    for j in arr:
        if(i + j == k):
            print(str(i) + " + " + str(j) +"= "+ str(k )) 
            break
arr_new= []       
#one pass
for i in range(0, len(arr)):
    arr_new.append(abs(arr[i] -17))

    
res= list(set(arr).intersection(arr_new))

if (len(res)>0):
    print(str(res[0]) + " + " + str(res[1]) +"= "+ str(k ))
else:
    print("No numbers add up to k")
    