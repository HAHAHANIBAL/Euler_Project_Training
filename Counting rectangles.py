#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #85

from math import sqrt
import sys

error=sys.maxint
closestarea=0
target=2000000

x=2000
y=1

while x>=y:
    rects=x*(x+1)*y*(y+1)/4
    if error>abs(rects-target):
        closestarea=x*y
        error=abs(rects-target)
    if rects>target:
        x-=1
    else:
        y+=1



print closestarea
