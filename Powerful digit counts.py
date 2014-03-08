#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #62

import math
result=0
lower=0
n=1
while lower<10:
    lower=int(math.ceil(math.pow(10,(n-1.0)/n)))
    result+=10-lower
    n+=1

print result