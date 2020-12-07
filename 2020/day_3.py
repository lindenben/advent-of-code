# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:16:32 2020

@author: LindenB
"""
import pandas as pd
with open(r"C:\Users\lindenb\OneDrive - Jacobs\Documents\Projects\R\Advent of Code\input_3a.txt", "r") as f:
    input_1 = [line.strip() for line in f]

#%%
counter = 0
line = 1
for i in input_1[1:]:
    i=i*1000000
    char = i[1*(line)]
    line +=1
    if char == '#':
        counter +=1
print(counter)

counter = 0
line = 1
for i in input_1[1:]:
    i=i*1000000
    char = i[3*(line)]
    line +=1
    if char == '#':
        counter +=1
print(counter)
 
counter = 0
line = 1
for i in input_1[1:]:
    i=i*1000000
    char = i[5*(line)]
    line +=1
    if char == '#':
        counter +=1
print(counter)
    
counter = 0
line = 1
for i in input_1[1:]:
    i=i*1000000
    char = i[7*(line)]
    line +=1
    if char == '#':
        counter +=1
print(counter)
   
#%%
counter = 0
line = 1
row = 0
for i in input_1[1:]:
    if (row % 2) == 0:
        row +=1
    else:
        print(i)
        i=i*1000000
        char = i[1*(line)]
        line +=1
        row +=1
        if char == '#':
            counter +=1
print(counter)