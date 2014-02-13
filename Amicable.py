#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

#Euler #21
import math
from pylab import *

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


prime=primelist(100)


def primefactorization(prime,num):
    remain=num
    sum=1
    p=prime[0]
    i=0
    while p*p<=remain and num>1 and i<len(prime):
        p=prime[i]
        i+=1
        if remain%p==0:
            j=p*p
            remain=remain/p
            while remain%p==0:
                j*=p
                remain=remain/p
            sum=sum*(j-1)/(p-1)
    if remain>1:
        sum*=remain+1
    return sum-num

divisors=primefactorization(prime,90)

print divisors

#faster version, use sieve to obtain all the divisible sums for all numbers<10000
limit=10000
div=[1]*limit

for i in range(2,limit/2):
    j=i
    while j<limit:
        if j!=i:
            div[j]+=i
        j+=i

print div[284]

