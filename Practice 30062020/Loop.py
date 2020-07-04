# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:32:05 2020

@author: hp
"""

sum_fin = 0.0
"""
for i1 in range (1,10,1):
    sum_fin = sum_fin + i1
    print("Value of i1 is :", i1, "while sum_fin is :", sum_fin, "\n")
 
for i2 in range (15):
    print("Value of i2 is : ", i2, "\n")
"""
string1 = "quek ying jie"
num_search = 0
var_search = "33"
for i3 in range(len(string1)):
    if string1[i3] == var_search:
        print("We found", var_search, "at", i3)
        num_search += 1
        
if num_search != 0:
    print("We found", num_search, "number of", var_search)   
else:
    print("We found nothing.")     

        
    