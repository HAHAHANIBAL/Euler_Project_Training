#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #41

import sympy

def ispandigital(number):
    digits=[]
    n=number
    while n:
        if n%10 not in digits and (n%10)<=int(str(number)[0]):
            digits.append(n%10)
        else:
            break
        n/=10
    if len(digits)==len(list(str(number))):
        return True
    else:
        return False

max=0
for i in range(7600000,7654321):
    if sympy.isprime(i):
        if ispandigital(i):
            #Pandigital does not contain 0 in this problem
            if '0' in str(i):
                continue
            else:
                max=i
print max

