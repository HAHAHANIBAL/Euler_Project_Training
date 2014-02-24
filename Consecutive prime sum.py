#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #50
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

prime=prime_list(1000000)
primesum=[0]*(len(prime)+1)
for i in range(1,len(prime)):
    primesum[i+1]=prime[i]+primesum[i]

ctr=0
for i in range(ctr,len(primesum)):
    for j in xrange(i-ctr-1,0,-1):
        if primesum[i]-primesum[j]>1000000:
            break
        if isprime(primesum[i]-primesum[j]):
            ctr=i-j
            result=primesum[i]-primesum[j]
            print i,j,ctr

print result, ctr