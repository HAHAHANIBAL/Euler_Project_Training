#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #43

def isuniquedigit(number):
    digit=[]
    length=len(str(number))
    while number:
        if number%10 not in digit:
            digit.append(number%10)
        else:
            break
        number/=10
    if len(digit)==length:
        return True
    else:
        return False


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

#Brute force sieve

for i in xrange(17,1000,17):
    if isuniquedigit(i):
        for j in xrange(13,1000,13):
            if j%100==i/10 and isuniquedigit(j):
                for k in xrange(11,1000,11):
                    if k%100==j/10 and isuniquedigit(k):
                        for l in xrange(7,1000,7):
                            if l%100==k/10 and isuniquedigit(l):
                                for m in xrange(5,1000,5):
                                    if m%100==l/10 and isuniquedigit(m):
                                        for n in xrange(3,1000,3):
                                            if n%100==m/10 and isuniquedigit(n):
                                                for o in xrange(2,1000,2):
                                                    if o%100==n/10 and isuniquedigit(o):
                                                        if o%100<10:
                                                            number=str(o/100)+'0'+str(o%100)+str(n%10)+\
                                                                  str(m%10)+str(l%10)+str(k%10)+str(j%10)+str(i%10)
                                                        else:
                                                            number=str(o/100)+str(o%100)+str(n%10)+\
                                                                  str(m%10)+str(l%10)+str(k%10)+str(j%10)+str(i%10)
                                                        if isuniquedigit(int(number)):
                                                            #one can find the number without
                                                            #duplicate numbers and add one missing digits
                                                            print number




