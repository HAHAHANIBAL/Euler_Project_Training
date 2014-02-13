#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #24
import math
limit=1000000
factor=1
digit=10
remain=limit
numbers=[0,1,2,3,4,5,6,7,8,9]


for i in range(0,10):
    n=1
    for j in range(1,digit-i):
        n*=j
    index=int(math.ceil(float(remain)/float(n)))
    print numbers[index-1]
    numbers.remove(numbers[index-1])
    remain=remain-remain/n*n


