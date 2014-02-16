#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #31
limit=200
coin=[1,2,5,10,20,50,100,200]
ways=[0]*201
ways[0]=1

for i in range(0,len(coin)):
    for j in range(coin[i],limit+1):
        ways[j]+=ways[j-coin[i]]

print ways[200]

#Euler #32
a=15
b=20
prod=a*b
def catnumber(a,b):
    return int(str(a)+str(b))
prod=catnumber(catnumber(prod,b),a)
print prod

number=12345899
def ispandigital(number):
    digits=[]
    n=number
    while n:
        if n%10 not in digits:
            digits.append(n%10)
        else:
            break
        n/=10

    if len(digits)==len(list(str(number))):
        return True
    else:
        return False

bol=ispandigital(number)
print bol