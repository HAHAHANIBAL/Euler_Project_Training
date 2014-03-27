#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #83


import sys
infinity = sys.maxint - 1

f = open("matrix.txt")
lines = f.readlines()
f.close()

matrix = map(lambda x: map(int, x.strip().split(",")), lines)
dim = len(matrix)

dist = dict()
previous = dict()
Q = set()

for i in range(dim):
    for j in range(dim):
        v = i * 100 + j
        dist[v] = infinity
        previous[v] = None
        Q.add(v)

dist[0] = 0

while len(Q) > 0:

    u = min(Q, key=lambda x: dist[x])
    Q.remove(u)

    neighbours = set()
    if u // 100 > 0: neighbours.add(u - 100)
    if u % 100 > 0: neighbours.add(u - 1)
    if u // 100 < dim - 1: neighbours.add(u + 100)
    if u % 100 < dim - 1: neighbours.add(u + 1)

    for v in neighbours:
        alt = dist[u] + matrix[v // 100][v % 100]
        if alt < dist[v]:
            dist[v] = alt
            previous[v] = u

total = matrix[0][0]
v = (dim - 1) * 100 + (dim - 1)
while v:
    total += matrix[v // 100][v % 100]
    v = previous[v]

print total