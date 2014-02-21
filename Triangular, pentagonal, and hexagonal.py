#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #45
from math import sqrt

#Hex is the subset of tri, so we only need to check if hex belongs to pent and we're good

def ispentagonal(number):
    pentagonal=(sqrt(1.0+24*number)+1.0)/6.0
    if pentagonal==int(pentagonal):
        return True
    else:
        return False


i=143
flg=True
while flg:
    i+=1
    hex=i*(2*i-1)
    if ispentagonal(hex):
        flg=False

print hex