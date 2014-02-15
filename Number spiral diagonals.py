#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
import math
#Euler #28
sum=1
last_base=1
iteration=math.floor(1000/2)


for i in range(0,int(iteration)):
    #calculate base distance
    length=i*2
    base=last_base
    n=1
    #loop four edges
    while n<5:
        base+=length
        n+=1
        last_base=base
        sum+=base

print sum



