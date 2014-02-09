#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

from pylab import *


sum=0

#Euler #1
for i in range(0,1000):
    if i%3==0 or i%5==0:
        sum+=i


print sum

#Euler #2
i=1
j=2
fib=0
sum=0

while fib<4000000:
    fib=i+j
    if fib%2==0:
        sum+=fib
    i=j
    j=fib


print sum+2

#Euler #3
n = 600851475143
i = 2
#a number can only have one prime factor whose value is larger than sqrt(n)
while i*i<n:
     while n%i == 0:
         n=n/i
     i=i+1

print n

#Euler #4
i=9
for j in range(0,9):
    for k in range(0,9):
        number=int(str(i)+str(j)+str(k)+str(k)+str(j)+str(i))
        for count in range(900,998):
            if number/count<1000 and number%count==0:
                print number

#Euler #5
i=0
#all prime factors
n=3*5*7*11*13*17*19
count=0
while i!=1:
    for j in range(2,20):
        count+=n%j
    if count==0:
        i=1
    n=n*3*2
    count=0

count=0
#delete additional 3s and 2s
n=n/3/3/3/3/2
for j in range(2,20):
    count+=n%j
print n
