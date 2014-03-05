#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #60

from math import sqrt
from sympy import isprime

def prime_list(limit):
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



limit = 10000

primes = prime_list(limit)

s1 = dict()
s2 = set()
s3 = set()
s4 = set()

for p in primes:
    s1[p] = set()

    for s in s1:
        if isprime(int(str(p) + str(s))) and isprime(int(str(s) + str(p))):
            s1[s].add(p)
            s1[p].add(s)
            s2.add((s, p))

    for s in s2:
        if p in s1[s[0]] and p in s1[s[1]]:
            s3.add((s[0], s[1], p))
    for s in s3:
        if p in s1[s[0]] and p in s1[s[1]] and p in s1[s[2]]:
            s4.add((s[0], s[1], s[2], p))
    for s in s4:
        if p in s1[s[0]] and p in s1[s[1]] and p in s1[s[2]] and p in s1[s[3]]:
            print p, s

