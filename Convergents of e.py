#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #65

limit=100
result=0

n_2=1
n_1=2

for i in range(2,limit+1):
    temp=n_2
    if i%3==0:
        c=2*(i/3)
    else:
        c=1
    n_2=n_1
    n_1=c*n_2+temp


def digitsum(n):
    sum=0
    while n!=0:
        sum+=n%10
        n/=10
    return sum

print digitsum(n_1)