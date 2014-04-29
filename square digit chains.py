#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #92

A=()
#print A
for i in range(1,568):
    k=str(i)
    while 1==1:
        s=0
        for j in k:
            s=s+(int(j))**2
        if s==89:
            A=A+([i,1],)
            break
        elif s==1:
            A=A+([i,0],)
            break
        k=str(s)

        count=1
for i in range(1,10000000):
    k=str(i)
    s=0
    for j in k:
        s=s+(int(j))**2
    if A[s-1][1]==1:
        count+=1
    if(i%20000)==0:
        print("Value of count is : ",count," for i=",i)
