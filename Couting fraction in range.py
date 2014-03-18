#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #73


limit=12000
t=0
l=[set() for i in range(limit+1)]
for i in xrange(2,limit/2):
    if len(l[i]):
        continue
    for j in xrange(i+i,limit+1,i):
        l[j].add(i)
for d in xrange(4,limit+1):
    for n in xrange(d/3+1,d/2+1):
        if d%n==0:
            continue
        if not len(l[d] and l[n]):
            t+=1
print t

