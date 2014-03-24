#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #80

#the looooong code
from math import sqrt
from decimal import *

getcontext().prec=105

print sum(map(int, list(''.join([str(Decimal(n).sqrt()).replace('.', '')[:100] for n in xrange(1, 100) if n not in [x*x for x in xrange(10)]]))))

#the easy code
getcontext().prec = 105
s = 0
for i in range(1, 101):
    if sqrt(i) != int(sqrt(i)):
        st = str(Decimal(i).sqrt())
        s += sum(int(c) for c in st.replace('.', '')[:100])
print s