#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #71

#Farey sequence
def fractionlessthan (ln, ld, rn, rd):
    return ln*rd < rn*ld

ln = 0
ld = 1
rn = 1
rd = 1
mn = 0
md = 0

while ld + rd <= 1000000:
    mn = ln + rn
    md = ld + rd
    left = (mn == 3 and md == 7) or not fractionlessthan(mn, md, 3, 7)

    if left:
        rn = mn
        rd = md
    else:
        ln = mn
        ld = md

print mn