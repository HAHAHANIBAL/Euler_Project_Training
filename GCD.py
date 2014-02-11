#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

import math
from pylab import *


length=75000
def primelist(length):
    limit=2000000
    crosslimit=int(sqrt(2000000))
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

    return prime[0:length-1]


prime=primelist(length)

def primefactorization(prime,num):
    count=1
    remain=num
    for i in range(0,len(prime)+1):
        #if this number is a prime itslef, it only has two primes
        if prime[i]*prime[i]>num:
            return count*2
        #if this number is divisible
        exponent=1
        while remain%prime[i]==0:
            exponent+=1
            remain=remain/prime[i]
        #total combinations of the prime exponent
        count*=exponent
        #if othing left, return the count
        if remain==1:
            return count

i=1
number=0
flg=1
while flg:
    number+=i
    i+=1
    if primefactorization(prime,number)>500:
        flg=0

print number


