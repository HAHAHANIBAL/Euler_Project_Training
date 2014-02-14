#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #26
import math

max1=0


for i in range(1,1000):
    number=i
    value=1
    position=0
    remain=[0]*1000

    while remain[value]==0 and value!=0:
        remain[value]=position
        value*=10
        value%=number
        position+=1
    if max(remain)>max1:
        max1=max(remain)


print max1