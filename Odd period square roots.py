#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #64

from math import sqrt
result=0
for i in range(2,10001):
    limit=int(sqrt(i))
    if limit*limit==i:
        continue
    period=0
    d=1
    m=0
    a=limit

    m=d*a-m
    d=(i-m*m)/d
    a=(limit+m)/d
    period+=1
    while a!=2*limit:
        m=d*a-m
        d=(i-m*m)/d
        a=(limit+m)/d
        period+=1

    if period%2==1:
        result+=1


print result