#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #30
power=[]
for i in range(0,10):
    power.append(i**5)
count=0

#the upper limit
upper=9**5*5

for i in range(2,upper):
    number=i
    sum=0
    while number>0:
        #calculate each the power of each digit
        d=number%10
        #reduce the number by one digit
        number/=10
        sum+=power[d]
    if sum==i:
        count+=i

print count
