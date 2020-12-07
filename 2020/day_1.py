# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:16:32 2020

@author: LindenB
"""

with open(r"C:\Users\lindenb\OneDrive - Jacobs\Documents\Projects\R\Advent of Code\input.txt", "r") as f:
    input_1 = [line.strip() for line in f]
    
#%%
for i in input_1:
    for j in input_1:
        for k in input_1:
            if int(i) + int(j) + int(k) == 2020:
                print(i)
                print(j)
                print(k)
                print(int(i)*int(j)*int(k))