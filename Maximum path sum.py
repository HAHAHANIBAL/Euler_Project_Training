#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #67
#construct matrix
Matrix = [[0 for x in xrange(100)] for x in xrange(100)]
j=0
with open('triangle2.txt','rb') as fin:
    for line in fin:
        i=0
        m=0
        flg=1
        while flg:
            Matrix[j][m]=int(line[i]+line[i+1])
            i+=3
            m+=1
            #judge whether it is EOL
            if i>(len(line)-2):
                flg=0
        j+=1
#dynamic programming
print Matrix

upper=100
#bottom up calculation of sums
for j in xrange(98,-1,-1):
    for i in range(1,upper):
        if Matrix[j+1][i-1]>Matrix[j+1][i]:
            Matrix[j][i-1]=Matrix[j][i-1]+Matrix[j+1][i-1]
        else:
            Matrix[j][i-1]=Matrix[j][i-1]+Matrix[j+1][i]
    #every loop shrink the size of the triangle once
    upper-=1
print Matrix[0]
