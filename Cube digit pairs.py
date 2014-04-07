#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #90

try:
    import psyco
    psyco.full()
except:
    pass

squares=['01','04','09','16','25','36','49','64','81']

def check(set1,set2):
        found=True
        set1,set2=set(set1),set(set2) #make them mutable
        if 6 in set1: set1.add(9)
        if 9 in set1: set1.add(6)
        if 6 in set2: set2.add(9)
        if 9 in set2: set2.add(6)
        for s in squares:
                digit1,digit2=int(s[0]),int(s[1])
                if digit1 in set1 and digit2 in set2: continue
                if digit1 in set2 and digit2 in set1: continue
                found=False
        return found

cube_sides=set()
for i in xrange(10):
        for j in xrange(i,10):
                for k in xrange(j,10):
                        for l in xrange(k,10):
                                for m in xrange(l,10):
                                        for n in xrange(m,10):
                                                if i < j < k < l < m < n:
                                                        cube_sides.add(frozenset([i,j,k,l,m,n]))

results=set()
for d1 in cube_sides:
        for d2 in cube_sides:
                if check(d1,d2): results.add(frozenset([d1,d2]))

print len(results)
