#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
import math

#Euler #13
numbers=[]
#read the number, it has no problem reading it in Python though..
with open('largeN.txt','rb') as fin:
    for line in fin:
        numbers.append(line)

sum=0
for i in range(0,100):

    sum+=int(numbers[i])

#slice the number
print str(sum)[:10]

#Euler #14
sequence=[0]*1000002
sequence[2]=1

for i in range(3,1000000):
    n=i
    while n!=1:
        if n%2==0:
            n=n/2
            #create a storage array that if encounter a previous number it automatically appends the sequence and quit
            if n<i:
                sequence[i]+=1
                sequence[i]+=sequence[n]
                n=1
            else:
                sequence[i]+=1
        elif n%2!=0:
            n=3*n+1
            sequence[i]+=1

max_idx=sequence.index(max(sequence))
print max_idx

#Euler #15
#this is basically a combination problem
total=40
step_down=20
paths=1

for i in range(0,20):
    paths*=total-i
    paths/=i+1

print paths

#The key to solve common divisible prime factors
print int(math.log(20)/math.log(2))