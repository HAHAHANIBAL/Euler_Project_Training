#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #47
from math import sqrt


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

prime=prime_list(100000)


def factors(number):
    count=0
    remain=number
    for i in range(0,len(prime)):
        if prime[i]**2>number:
            count+=1
            return count
        flg=False
        while remain%prime[i]==0:
            flg=True
            remain=remain/prime[i]
        if flg:
            count+=1
        if remain==1:
            return count
    return count

con_count=0
start=100000
while con_count<4:
    start+=1
    if factors(start)>=4:
        con_count+=1
    else:
        con_count=0

print start-3







