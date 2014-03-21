#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #77
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


primes=primelist(1000)
target=2

while True:
    ways=[0 for i in range(0,target+1)]
    ways[0]=1
    for i in range(0,len(primes)):
        for j in range(primes[i],target+1):
            ways[j]+=ways[j-primes[i]]
    if ways[target]>5000:
        break
    target+=1

print target
