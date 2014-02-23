#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #48
#Brute force runs very fast under Python, not sure about other language though
sum=0
for i in range(1,1001):
    sum+=i**i

print sum%10000000000
