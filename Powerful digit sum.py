#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #56
import math


def digitsum(number):
    k=list(str(number))
    sum=0
    for i in range(0,len(k)):
        sum+=int(k[i])
    return sum

limit=100
result=0


#calculate the total digits of the pow can be acheive by log10(a^b)

for a in xrange(limit-1,0,-1):
    for b in xrange(limit-1,0,-1):
        number=int(a**b)
        if int(math.log10(number))*9<result:
            break
        temp=digitsum(number)
        print result
        if temp>result:
            result=temp

print result
