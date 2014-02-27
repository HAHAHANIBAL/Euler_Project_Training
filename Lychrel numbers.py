#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #55

def ispalindrome(number):
    return str(number)==str(number)[::-1]

def reverse(num):
    reverse=str(num)[::-1]
    return reverse

def islychrel(num):
    temp=num
    for i in range(0,50):
        temp+=int(reverse(temp))
        if ispalindrome(temp):
            return False
    return True

result=0
for i in range(10,10000):
    if islychrel(i):
        result+=1

print result






