#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #82


matrix = [[int(i) for i in line.split(',')] for line in open("matrix.txt", 'r').read().split('\n')]
size, solution = len(matrix), [0 for y in xrange(0, len(matrix))]
for y in xrange(0, size):
    solution[y] = matrix[y][size - 1]
for x in xrange(size - 2, -1, -1):
    solution[0] += matrix[0][x]
    for y in xrange(1, size):
        solution[y] = matrix[y][x] + min(solution[y - 1], solution[y])
    for y in xrange(size - 2, -1, -1):
        solution[y] = min(solution[y], solution[y + 1] + matrix[y][x])
print min(solution)