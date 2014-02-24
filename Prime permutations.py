#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #49
from math import sqrt
from sympy import isprime
import numpy


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

prime=prime_list(10000)
prime=prime[prime.index(1009):]

def ispermutation(num1,num2):
    array=[0]*10
    while num1!=0:
        array[num1%10]+=1
        num1/=10
    while num2!=0:
        array[num2%10]-=1
        num2/=10
    for i in range(0,10):
        if array[i]!=0:
            return False

    return True

for i in range(0,len(prime)):
    for j in range(i+1,len(prime)):
        k=prime[j]+(prime[j]-prime[i])
        if k<10000 and isprime(k):
            if ispermutation(prime[i],prime[j]) and ispermutation(prime[i],k):
                final=str(prime[i])+str(prime[j])+str(k)
                break


print final