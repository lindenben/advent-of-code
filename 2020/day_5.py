# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:16:32 2020

@author: LindenB
"""
import pandas as pd 
with open(r"C:\Users\lindenb\OneDrive - Jacobs\Documents\Projects\R\Advent of Code\input_5a.txt", "r") as f:
    input_1 = [line.strip() for line in f]
#%%

counter = 0
list_1 = []
for i in input_1:
    row = 0
    col = 0
    it = 64
    for j in i[:7]:
        if j == 'B':
            row = row + it
        it = it/2
    it = 4
    for j in i[7:]:
        if j == 'R':
            col = col + it
        it = it/2
    list_1.append((row*8)+col)

possible = []   
for i in range(0,128):
    for j in range(0,8):
        if (((i*8)+j) < max(list_1)) & (((i*8)+j) > min(list_1)):
            possible.append((i*8)+j)

for i in possible:
    if i not in list_1:
        print(i)
    
    
    
    
    
    
    
    
    
    
    
    