#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

Matrix = [[0 for x in xrange(21)] for x in xrange(21)]
i=1

#read 2-D matrix delimiter=' ' into a 2-D array
with open('numbers.txt','rb') as fin:
    for line in fin:
        k=1
        for j in xrange(1,60,3):
            Matrix[i][k]=int(line[j-1]+line[j]+line[j+1])
            k+=1
        i+=1

#check horizontal
max_bak_diag=0
max_diag=0
max_rows=0
max_cols=0
for i in range(1,21):
    for j in range(1,21):
        #check backward diagonal
        if i<=16 and j>=4:
            n=Matrix[i][j]*Matrix[i+1][j-1]*Matrix[i+2][j-2]*Matrix[i+3][j-3]
            if n>max_bak_diag:
                max_bak_diag=n
        #check diagonal
        if i<=16 and j<=16:
            n=Matrix[i][j]*Matrix[i+1][j+1]*Matrix[i+2][j+2]*Matrix[i+3][j+3]
            if n>max_diag:
                max_diag=n
        #check rows
        if j<=16:
            n=Matrix[i][j]*Matrix[i][j+1]*Matrix[i][j+2]*Matrix[i][j+3]
            if n>max_rows:
                max_rows=n
        #check rows
        if i<=16:
            n=Matrix[i][j]*Matrix[i+1][j]*Matrix[i+2][j]*Matrix[i+3][j]
            if n>max_cols:
                max_cols=n

print max_bak_diag, max_diag, max_cols, max_rows