#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #57

import math
limit=1000
count=0

den=2
num=3

for i in range(1,limit):
    num+=2*den
    den=num-den
    if int(math.log10(num))>int(math.log10(den)):
        count+=1


print count


