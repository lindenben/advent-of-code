# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:16:32 2020

@author: LindenB
"""
import pandas as pd
with open(r"C:\Users\lindenb\OneDrive - Jacobs\Documents\Projects\R\Advent of Code\input_2.txt", "r") as f:
    input_1 = [line.strip() for line in f]

df = pd.DataFrame(input_1,columns =['input'])

df[['condition', 'input']] = df['input'].str.split(' ', 1, expand=True)

df[['letter', 'password']] = df['input'].str.split(':', 1, expand=True)

df[['min', 'max']] = df['condition'].str.split('-', 1, expand=True)
#%%
counter = 0
for i in range(len(df)):
    row = df.loc[i]
    if (row['password'].count(row['letter']) >= int(row['min'])) & (row['password'].count(row['letter']) <= int(row['max'])):
        counter +=1
        
#%%
counter = 0
for i in range(len(df)):
    counter_2 = 0
    row = df.loc[i]
    if row['password'].strip()[int(row['min'])-1] == row['letter']:
            counter_2 +=1

    if row['password'].strip()[int(row['max'])-1] == row['letter']:
            counter_2 +=1
    if counter_2 == 1:
        counter +=1
    