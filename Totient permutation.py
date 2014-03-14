#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #70
from math import sqrt

ratio=float("inf")

minimum, minimum_p = 10 ** 7, 0


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

primes=primelist(5000)
primes_new=[]
for item in primes:
    if item>2000:
        primes_new.append(item)

primes=primes_new

for p1 in primes:
    for p2 in primes:
        p = p1 * p2
        if p < 10 ** 7:
            totient = (p1 - 1) * (p2 - 1)
            if sorted(str(p)) == sorted(str(totient)):
                if float(p) / float(totient) < minimum:
                    minimum = float(p) / float(totient)
                    minimum_p = p
print minimum_p
