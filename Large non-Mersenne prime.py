#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #97

import time
start_time = time.clock()

x = 28433*2**7830457 + 1

x = x % 10**10

print x

print "Runtime of ",time.clock() - start_time ,"seconds"