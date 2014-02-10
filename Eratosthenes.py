#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
from pylab import *

limit=2000000
crosslimit=int(sqrt(2000000))
sieve=[False]*(limit+1)
for i in xrange(4,limit+1,2):
    sieve[i]=True

for i in xrange(3,crosslimit+1,2):
    if not sieve[i]:
        for m in xrange(i*i,limit+1,2*i):
            sieve[m]=True

