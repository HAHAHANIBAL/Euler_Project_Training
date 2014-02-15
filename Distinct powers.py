#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #29
distinct=[]
for a in range(2,101):
    for b in range(2,101):
        key=a**b
        if key not in distinct:
            distinct.append(key)
print len(distinct)
