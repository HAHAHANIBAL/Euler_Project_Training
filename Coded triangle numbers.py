#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #42
import re

fin=open('words.txt','r')
pat=re.compile(r'\"(\w+)\"')
for line in fin:
    name_list=pat.findall(line)

sorted_name=[]
for item in sorted(name_list):
    sorted_name.append(item)


triangle=[]
for i in range(1,100):
    triangle.append(int(0.5*i*(i+1)))

count=0

for item in sorted_name:
    score=0
    for i in range(0,len(item)):
        score+=ord(item[i])-64
    if score in triangle:
       count+=1

print count
