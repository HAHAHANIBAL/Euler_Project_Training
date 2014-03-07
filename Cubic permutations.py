#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #62

from collections import Counter

#Generate a lists of cubes with digts sorted
scubes=[''.join(sorted(str(x**3))) for x in range(100, 9000)]
#use Counter function to generate the most appearances sorted digits from hash table
top=Counter(scubes).most_common(1)


cubes=[str(x**3) for x in range(100, 9000)]

for c in cubes:
   if ''.join(sorted(c)) == top[0][0]:
      print c
      break