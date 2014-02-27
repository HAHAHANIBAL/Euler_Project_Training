#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #52


def ispermutation(num1,num2):
    #this can be done in three ways: 1.itertools, 2.str/int conversion and 3.pure math array index
    array=[0]*10
    while num1!=0:
        array[num1%10]+=1
        num1/=10
    while num2!=0:
        array[num2%10]-=1
        num2/=10
    for i in range(0,10):
        if array[i]!=0:
            return False

    return True

ini=1
flg=1

while flg:
    ini*=10
    for i in range(ini,ini*10/6):
        flg=0
        for j in range(2,7):
            if not ispermutation(i,j*i):
                flg=1
                break
        if flg==0:
            result=i
            break

print result
