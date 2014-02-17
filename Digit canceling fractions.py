#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #33

den=1
nom=1

for i in range(1,10):
    for d in range(1,i):
        for n in range(1,d):
            if (n*10+i)*d==n*(i*10+d):
                den*=d
                nom*=n

print den, nom
print den/8

#Euler #34
def fact(n):
    for i in range(1,n):
        n*=i
    return n

factor=[]
for i in range(0,10):
    if i==0:
        factor.append(1)
    else:
        factor.append(fact(i))
print factor


final=0
for i in range(10,2540161):
    sumfact=0
    number=i
    while number!=0:
        d=number%10
        number/=10
        sumfact+=factor[d]
    if sumfact==i:
        final+=sumfact


print final
