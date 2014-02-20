#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #40

import sympy

multiplier=1
result=''
final=1
cri=multiplier
for item in xrange(1,1000000):
    result+=str(item)
    if len(result)>multiplier:
        final*=int(str(result)[multiplier-1])
        multiplier*=10

print final

