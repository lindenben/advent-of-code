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
                yield ' '.join(ret)
                ret = []
        else:
            ret.append(line.rstrip())
    if ret:
        yield ''.join(ret)

with open(r"C:\Users\lindenb\OneDrive - Jacobs\Documents\Projects\R\Advent of Code\input_4a.txt", 'r') as f:
    s = list(per_section(f))
    df = pd.DataFrame({'data':s})
    print (df)

df['data'] = df['data'].str.replace('cid:',' ')
#%%
counter = 0
valid = pd.DataFrame()
for i in df['data']:
    count = 0
    for j in i:
        if j == ':':
            count +=1
    if count == 7:
        valid = valid.append(pd.DataFrame({'data':pd.Series(i)}))
        counter +=1

print(counter)

import re
counter = 0
for i in valid['data']:
    count = 0
    byr = i.split('byr:')[1].split(' ')[0]
    iyr = i.split('iyr:')[1].split(' ')[0]
    eyr = i.split('eyr:')[1].split(' ')[0]
    hgt = i.split('hgt:')[1].split(' ')[0]
    if '#' in i.split('hcl:')[1].split(' ')[0]:
        hcl = re.sub('[^a-f0-9]+', '', i.split('hcl:')[1].split(' ')[0].split('#')[1])
    else:
        hcl = 'a'
    ecl = i.split('ecl:')[1].split(' ')[0]
    pid = i.split('pid:')[1].split(' ')[0]
    if len(pid) > 9:
        pid = 'a'
        print(pid)
    pid = re.sub('[^0-9]+', '', pid)
    
    if (int(byr)>1919) & (int(byr)<2003):
        count +=1
    if (int(iyr)>2009) & (int(iyr)<2021):
        count +=1
    if (int(eyr)>2019) & (int(eyr)<2031):
        count +=1
    if hgt[-2:] == 'in':
        if (int(hgt[:-2]) > 58) & (int(hgt[:-2]) < 77):
            count +=1
    if hgt[-2:] == 'cm':
        if (int(hgt[:-2]) > 149) & (int(hgt[:-2]) < 194):
            count +=1
    if len(hcl) == 6:
        count +=1
    if ecl in ['amb','blu','brn','gry','grn','hzl','oth']:
        count +=1
    if len(pid) == 9:
        count +=1

    if count == 7:
        counter +=1
print(counter)     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        