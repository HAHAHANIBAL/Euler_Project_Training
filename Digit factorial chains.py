#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #74

factdict = { '0':1 }
for i in xrange(1, 10):
    factdict[str(i)] = i * factdict[str(i-1)]

def dfactsum(n):
    global factdict
    ds=str(n)
    return sum([factdict[d] for d in ds])

def chainlen(n, cache={}):
    if n in cache:
        return n

    chain=set([n])

    fs = dfactsum(n)
    while (fs not in chain) and (fs not in cache):
        chain.add(fs)
        fs = dfactsum(fs)

    chainlen = len(chain)
    if fs in cache:
        chainlen += cache[fs]

    cache[n] = chainlen

    return cache[n]

count = 0
for i in xrange(0, 1000000):
    if chainlen(i) == 60:
        count += 1

print count
