#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #86

from math import sqrt
l=2
count=0
target=1000000

while count<target:
    l+=1
    for wh in range(3, 2*l+1):
        root=sqrt(wh*wh+l*l)
        if root==int(root):
            if wh<=l:
                count+=wh/2
            else:
                count+=(l+(l-(wh+l)/2))

