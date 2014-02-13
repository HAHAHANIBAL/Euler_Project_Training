#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #25
import math

fib1=1
fib2=1
fib=fib1+fib2
count=2

while len(str(fib))<1000:
    count+=1
    fib=fib1+fib2
    fib1=fib2
    fib2=fib

print count