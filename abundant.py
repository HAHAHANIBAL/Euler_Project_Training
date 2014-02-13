#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #23

limit=28123
div=[1]*limit

for i in range(2,limit/2):
    j=i
    while j<limit:
        if j!=i:
            div[j]+=i
        j+=i

abundant_num=[]
for i in range(2,len(div)):
    if div[i]>i:
        abundant_num.append(i)


abundant_sum=[False]*28123

for i in range(0,len(abundant_num)):
    for j in range(i,len(abundant_num)):
        if abundant_num[i]+abundant_num[j]<28123 and not abundant_sum[(abundant_num[i]+abundant_num[j])]:
            abundant_sum[(abundant_num[i]+abundant_num[j])]=True
        elif abundant_num[i]+abundant_num[j]>28123:
            break

print abundant_sum