#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #68

import itertools

def check_rings(outer, inner):
    sm = [0] * len(inner)
    for a in range(len(inner)):
        for b in range(len(outer)):
            sm[b] = outer[b] + inner[(a+b-1)%len(inner)] + inner[(a+b)%len(inner)]
        av = sum(sm) / len(sm)
        if all([s == av for s in sm]):
            return a
    return -1


start = [6]
outer = [7, 8, 9, 10]
inner = range(1,6)

outer_rings = []
for p in itertools.permutations(outer):
    outer_rings.append(start + list(p))
inner_rings = [p for p in itertools.permutations(inner)]
answers = []
for ou in outer_rings:
    for inn in inner_rings:
        start_index = check_rings(ou, inn)
        if start_index >= 0:
            ds = ""
            for i in range(len(ou)):
                ds = ds + str(ou[i])
                for j in range(2):
                    ds = ds + str(inn[(i+j-1)%len(inner)])
            answers.append(int(ds))
print max(answers)
