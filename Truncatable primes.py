#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #37

import sympy
#can be further reduce to [1,2,3,5,7,9] and [3,7]
#in the prime number 2 and 5 are impossible for right hand truncate
#in the append list 4,6,8 are impossible because they are (1) not primes and (2) are divisible for right hand truncate
appends=[1,2,3,5,7,9]
candidate=[3,7]
sum=0
count=0
while count<11:
    prime=candidate[0]
    #pop out the first elements of the lists
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
            #loop termination control
            count+=1
        for i in range(0,len(appends)):
            #generate the new candidate lists and loop again
            candidate.append(multiplier*appends[i]+prime)
print sum