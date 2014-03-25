#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #81

import sys

if len(sys.argv) < 2:
        print "usage: mps <grid_file>"
        exit(1)

fn = sys.argv[1]
with open(fn) as f:
        grid = [map(int, line.split(',')) for line in f.readlines()]

costs = []
for row in grid:
        costs.append([0] * len(row))

for y in xrange(-1, -len(grid)-1, -1):
        for x in xrange(-1, -len(grid[y])-1, -1):
                neighbors = (costs[y][x+1], costs[y+1][x])
                costs[y][x] = grid[y][x] + (min(neighbors) if x < -1 and y < -1 else sum(neighbors))

print costs[0][0]
