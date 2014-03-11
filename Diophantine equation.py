#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #66

from math import *
#Pell's Equation
result = 0
xmax = 0
#find convergents of sqrt(D)
#loop over the loop until numerator**2-D*denominator**2=1
#the numerator is the answer
for i in range(2,1001):
    limit=int(sqrt(i))
    if limit*limit==i:
        continue
    m=0
    d=1
    a=limit
    numm1=1
    num=a
    denm1=0
    den=1
    while num*num-i*den*den!=1:
        m=d*a-m
        d=(i-m*m)/d
        a=(limit+m)/d
        numm2=numm1
        numm1=num
        denm2=denm1
        denm1=den
        num=a*numm1+numm2
        den=a*denm1+denm2
    if num>xmax:
        xmax=num
        result=i

print xmax, result



