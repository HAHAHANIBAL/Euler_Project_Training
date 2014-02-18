#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #37

import sympy
#can be further reduce to [1,2,3,5,7,9] and [3,7]
appends=[1,2,3,4,5,6,7,8,9]
candidate=[2,3,5,7]
sum=0
count=0
while count<11:
    prime=candidate[0]
    candidate.remove(prime)
    if sympy.isprime(prime):
        istruncate=True
        n=prime
        multiplier=1
        while n>0:
            istruncate=sympy.isprime(n) and istruncate
            n/=10
            multiplier*=10
        if istruncate and prime>10:
            sum+=prime
            count+=1
            print prime
        for i in range(0,len(appends)):
            candidate.append(multiplier*appends[i]+prime)
print sum