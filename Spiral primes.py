#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #58

from sympy import isprime

num_prime=3
length=2
c=9

while float(num_prime)/(2*float(length)+1)>0.1:
    length+=2
    for i in range(0,3):
        c+=length
        if isprime(c):
            num_prime+=1
    c+=length

print length+1