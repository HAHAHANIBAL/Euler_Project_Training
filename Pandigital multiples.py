#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #38
#it's all about reducing the search spaces---typical Euler problems
def catnumber(a,b):
    return int(str(a)+str(b))

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

#all multplications can be written in the form as x*1*y*2 test in order get a 9 in 9-digit pandigital, how much should
# we get
#You can not do digits larger than 5 because n>1, 5-digits number will at least render 10 digits results
for x in xrange(9387,9000,-1):
    digit=catnumber(x,x*2)
    if ispandigital(digit):
        #Pandigital does not contain 0 in this problem
        if '0' in str(digit):
            continue
        else:
            break
print digit