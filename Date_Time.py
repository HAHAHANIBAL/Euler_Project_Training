#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #19&#20
import datetime
sunday=0

for year in range(1901,2001):
    for month in range(1,13):
        if datetime.datetime(year,month,1).weekday()==6:
            sunday+=1

print sunday

number=1
sum=0
for i in range(1,101):
    number*=i
n=number
while n:
    #sum up all digits one by one
    sum+=n%10
    n/=10
print sum