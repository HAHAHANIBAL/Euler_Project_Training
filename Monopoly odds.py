#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #84

import numpy as np

# Constants
J = 10	# Jail
GJ = 30	# Go to Jail
RR = [ 5, 15, 25, 35 ]	# Rail roads
CC = [ 2, 17, 33 ]	# Community Chest
CH = [ 7, 22, 36 ]	# Chance

## Helpers
def nextRR(n):#{{{
    if n < 5:
        return 5
    elif n < 15:
        return 15
    elif n < 25:
        return 25
    elif n < 35:
        return 35
    return 5#}}}

def nextU(n):#{{{
    if n < 12:
        return 12
    if n < 28:
        return 28
    return 12#}}}

# Setup Transition Matrix
A = np.zeros((40,40))

## Add die roll probabilities
for n in range(40):
    A[(n+2) %40][n] = 1./16
    A[(n+3) %40][n] = 2./16
    A[(n+4) %40][n] = 3./16
    A[(n+5) %40][n] = 4./16
    A[(n+6) %40][n] = 3./16
    A[(n+7) %40][n] = 2./16
    A[(n+8) %40][n] = 1./16

## Fix Go to jail by 3 doubles
## and Go to jail
for n in range(40):
    A[J][n] += (1./4)**3
    A[(n+2) %40][n] *= 1 - (1./1)*(1./4)**2
    A[(n+4) %40][n] *= 1 - (1./3)*(1./4)**2
    A[(n+6) %40][n] *= 1 - (1./3)*(1./4)**2
    A[(n+8) %40][n] *= 1 - (1./1)*(1./4)**2
    A[J][n] += A[GJ][n]
    A[GJ][n] = 0

for n in range(40):
## Fix Chance
    for ch in CH:
        if A[ch][n] == 0: continue
        rr = nextRR(ch)
        u = nextU(ch)
        A[0 ][n] += A[ch][n] * (1./16)
        A[J ][n] += A[ch][n] * (1./16)
        A[11][n] += A[ch][n] * (1./16)
        A[24][n] += A[ch][n] * (1./16)
        A[39][n] += A[ch][n] * (1./16)
        A[5 ][n] += A[ch][n] * (1./16)
        A[rr][n] += A[ch][n] * (2./16)
        A[u ][n] += A[ch][n] * (1./16)
        A[ch-3][n]+= A[ch][n] * (1./16)
        A[ch][n] = A[ch][n] * (6./16)
## Fix Community Chest
for cc in CC:
    if A[cc][n] == 0: continue
    A[0 ][n] += A[cc][n] * (1./16)
    A[J ][n] += A[cc][n] * (1./16)
    A[cc][n] = A[cc][n] * (14./16)

## Print the Matrix
# for n, row in enumerate(A):
# print '%02d\t'%n, ' '.join('%0.2f'%x for x in row)


## These 4 lines find the eigenvector of A
## associated with eigenvalue 1
## Alt. Paramaterize Kernel of A-I
u, s, vh = np.linalg.svd(A-np.identity(40))
null_mask = (s <= 1e-3)
null_space = np.compress(null_mask, vh, axis=0)
eigenvec = null_space[0] / sum(null_space[0]) # normalize the result so probabilities sum to 1

# Print the list of probabilities
for x, y in sorted(enumerate(eigenvec), key=lambda x:-x[1]):
print '%02d'%x, '%0.4f'%y
