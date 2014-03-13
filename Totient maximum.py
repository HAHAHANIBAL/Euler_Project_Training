#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #69
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

primes=primelist(200)
result=1
i=0
limit=1000000

while result*primes[i]<limit:
    result*=primes[i]
    i+=1

print result