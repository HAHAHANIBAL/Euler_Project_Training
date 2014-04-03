#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #88

def rek(n0,n,a,s,k):
      if n>1:
            j=d0[n]
            while d[n][j]>a:
                  j=j-1
            while j>0:
                  rek(n0,n//d[n][j],d[n][j],s-d[n][j],k+1)
                  j=j-1
      else:
            if k+s<=c and (b[k+s]==0 or b[k+s]>n0):
                  b[k+s]=n0


c=12000
b=[0]*(c+1)
c0=13000
d=[[0]*100 for i in range (c0)]
d0=[0]*c0
for i in range (1,c0):
      d0[i]=0
      d[i][0]=1
      k=2
      while k*k<=i:
            if i%k==0:
                  d0[i]+=1
                  d[i][d0[i]]=k
            k=k+1
for i in range (1,c0):
      k=d0[i]
      for j in range (k,-1,-1):
            if i//d[i][j]!=d[i][j]:
                  d0[i]+=1
                  d[i][d0[i]]=i//d[i][j]
for i in range (4,c0):
      if d0[i]>1:
            rek(i,i,i-1,i,0)
b.sort()
x=0
for i in range (1,c+1):
      if b[i]!=b[i-1]:
            x=x+b[i]
print(x)
