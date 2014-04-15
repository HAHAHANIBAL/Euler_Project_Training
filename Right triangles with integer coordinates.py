#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #91
import math


def gcd(a, b):
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    while x % y != 0:
        temp = x
        x = y
        y = temp % x
    return y

size = 50
result = size*size*3
for x in range(1, size+1):
    for y in range(1, size+1):
        fact = gcd(x, y)
        result += min(y*fact/x, (size-x)*fact/y) * 2

print result
