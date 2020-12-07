# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:16:32 2020

@author: LindenB
"""
import pandas as pd 
def per_section(it, is_delimiter=lambda x: x.isspace()):
    ret = []
    for line in it:
        if is_delimiter(line):
            if ret:
                yield ''.join(ret)
                ret = []
        else:
            ret.append(line.rstrip())
    if ret:
        yield ''.join(ret)

with open(r"C:\Users\lindenb\OneDrive - Jacobs\Documents\Projects\R\Advent of Code\input_6a.txt", 'r') as f:
    s = list(per_section(f))
    df = pd.DataFrame({'data':s})
    print (df)


#%%
from collections import OrderedDict
counter = 0
list_1 = []
for i in df['data']:
    counter = counter + len(''.join(OrderedDict.fromkeys(i.replace(' ','')).keys()))
print(counter) 
    
#%%
import pandas as pd 
def per_section(it, is_delimiter=lambda x: x.isspace()):
    ret = []
    for line in it:
        if is_delimiter(line):
            if ret:
                yield ':'.join(ret)
                ret = []
        else:
            ret.append(line.rstrip())
    if ret:
        yield ''.join(ret)

with open(r"C:\Users\lindenb\OneDrive - Jacobs\Documents\Projects\R\Advent of Code\input_6a.txt", 'r') as f:
    s = list(per_section(f))
    df = pd.DataFrame({'data':s})
    print (df)

#%%

counter = 0
list_1 = []
for i in df['data']:
    answers = i.split(':')
    count = 0
    for j in 'abcdefghijklmnopqrstuvwxyz':
        ans_count = sum(j in s for s in answers)
        if ans_count == len(answers):
            count = count + 1
        
    list_1.append(count)
print(sum(list_1)) 
    
    
    
    
    
    
    
    