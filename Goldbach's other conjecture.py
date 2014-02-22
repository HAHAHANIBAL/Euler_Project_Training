#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #46
from math import sqrt

def primelist(limit):
    crosslimit=int(sqrt(limit))
    sieve=[False]*(limit+1)
    for i in xrange(4,limit+1,2):
        sieve[i]=True

    for i in xrange(3,crosslimit+1,2):
        if not sieve[i]:
            #cross out all the odd m multipliers
            for m in xrange(i*i,limit+1,2*i):
                sieve[m]=True

    prime=[]
    for i in range(2,limit+1):
        if not sieve[i]:
            prime.append(i)

    return prime


prime=primelist(10000)

def istwicesqure(number):
    square=sqrt(float(number)/2)
    if square==int(square):
        return True
    else:
        return False

odd=1
result=False
while not result:
    #odd number generator
    odd+=2
    i=0
    result=True
    while odd>=prime[i]:
        if istwicesqure(odd-prime[i]):
            result=False
            break
        i+=1
print odd


