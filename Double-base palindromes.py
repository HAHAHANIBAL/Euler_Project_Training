#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #36

def binarypalindromes(number):
    binary1=''
    binary2=''
    while number:
    #backwards
        binary1+=str(number%2)
        binary2=str(number%2)+binary2
        number/=2
    if str(binary1)==str(binary2):
        return True
    else:
        return False


palin=[]
#Odd generator
for n in range(1,1000):
    dromes=n
    n/=10
    while n>0:
        dromes=dromes*10+(n%10)
        n/=10
    palin.append(dromes)
#Even generator
for n in range(1,1000):
    dromes=n
    while n>0:
        dromes=dromes*10+(n%10)
        n/=10
    palin.append(dromes)

sum=0

print palin
for n in palin:
    if binarypalindromes(n):
        sum+=n
    else:
        continue

print sum