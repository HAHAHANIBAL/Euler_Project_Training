#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #22
import re

fin=open('names.txt','r')
pat=re.compile(r'\"(\w+)\"')
for line in fin:
    print pat.findall(line)
    name_list=pat.findall(line)

sorted_name=[]
for item in sorted(name_list):
    sorted_name.append(item)

score=0
sum=0
index=1
for item in sorted_name:
    for i in range(0,len(item)):
        score+=ord(item[i])-64
    sum+=score*index
    index+=1
    score=0

print sum