#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #65

limit=100
result=0

d=1
n=2

for i in range(2,limit+1):
    temp=d
    if i%3==0:
        c=2*(i/3)
    else:
        c=1
    d=n
    n=c*d+temp


def digitsum(n):
    sum=0
    while n!=0:
        sum+=n%10
        n/=10
    return sum

print digitsum(n)