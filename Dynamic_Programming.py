#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

#Euler #18
#construct matrix
Matrix = [[0 for x in xrange(15)] for x in xrange(15)]
j=0
with open('Triangle.txt','rb') as fin:
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

upper=15
#bottom up calculation of sums
for j in xrange(13,-1,-1):
    for i in range(1,upper):
        if Matrix[j+1][i-1]>Matrix[j+1][i]:
            Matrix[j][i-1]=Matrix[j][i-1]+Matrix[j+1][i-1]
        else:
            Matrix[j][i-1]=Matrix[j][i-1]+Matrix[j+1][i]
    #every loop shrink the size of the triangle once
    upper-=1
print Matrix[0]