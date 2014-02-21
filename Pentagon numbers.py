#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #44
from math import sqrt
def ispentagonal(number):
    pentagonal=(sqrt(1.0+24*number)+1.0)/6.0
    if pentagonal==int(pentagonal):
        return True
    else:
        return False

notfound=True
sum=0
n=0
while notfound:
    n+=1
    pen1=int(n*(3*n-1)/2)
    for i in xrange(n-1,0,-1):
        pen2=int(i*(3*i-1)/2)
        if ispentagonal(pen1-pen2) and ispentagonal(pen1+pen2):
            sum=pen1-pen2
            notfound=False
            break


print n,i,pen1-pen2