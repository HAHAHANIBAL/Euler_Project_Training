#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #53

import itertools

sum=0

a=list(itertools.combinations('12345',3))


#caching factorials up to 100
def fact(n):
    cache=[1]*(n+1)
    for i in range(1,n+1):
        cache[i]=cache[i-1]*i
    return cache

count=0
#declare an array for all factorials up to 100
fac=fact(100)

#we don't have to loop functions over and over again because of the cache
for i in range(1,101):
    for j in range(1,i):
        if fac[i]/(fac[j]*fac[i-j])>=1000000:
            count+=1


print count

#pascal triangle solutions
limit=1000000
nlimit=100
sum=0

#create a 2-D pascal triangle matrix
pascal=[[0 for x in xrange(nlimit+1)] for x in xrange(nlimit+1)]

for i in range(0,nlimit+1):
    pascal[i][0]=1

for i in range(1,nlimit+1):
    for j in range(1,i+1):
        pascal[i][j]=pascal[i-1][j]+pascal[i-1][j-1]
        if pascal[i][j]>limit:
            #avoid using really long numbers, substitute all numbers larger than limit to limit
            pascal[i][j]=limit
            sum+=1
print sum
