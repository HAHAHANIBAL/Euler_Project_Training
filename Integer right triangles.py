#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #39

from math import sqrt



maxcount=0
sum=[]
for c in xrange(400,1,-1):
    count=0
    for b in xrange(c-1,0,-1):
        if len(str(sqrt(c**2-b**2)%10))==3:
            count+=1
            sum.append(b+c+int(sqrt(c**2-b**2)))
    if count>maxcount:
        maxcount=count

#return the parameter with most appearances
print max(set(sum),key=sum.count)

