#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #87

import time

start = time.time()

upper_limit = 50000000
# a is highest square root, b is highest cube root, c is highest 4th root
a = int(upper_limit**0.5)
b = int(upper_limit**(float(1)/float(3)))
c = int(upper_limit**0.25)

def primesieve(n):
    initSieve = []
    maxNum = int(n**0.5)+1
    for i in range(2,n):
        initSieve.append(True)
    j = 2
    while j <= maxNum:
        if initSieve[j-2]:
            for k in range(j*j, n, j):
                initSieve[k-2] = False
        j += 1
    outputList = [x+2 for x in range(len(initSieve)) if initSieve[x]]
    return outputList

factors = primesieve(a)  #all primes up to highest square root

squares = [x**2 for x in factors if x <= a]
cubes = [x**3 for x in factors if x <= b]
fourths = [x**4 for x in factors if x <= c]

##brute force - test every combination

answers = set()
for i in fourths:
    for j in cubes:
        ij = i+j
        if ij >= upper_limit:
            break
        for k in squares:
            test = ij + k
            if test >= upper_limit:
                break
            answers.add(test)

print len(answers)
end = time.time() - start
print 'It took %f seconds' % end