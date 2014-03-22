#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #78

limit = 10 ** 5
divisor = 1000000

p = [0] * limit
p[0] = 1

for i in range(1, limit):
   j = 1; k = 1; s = 0
   while j > 0:
      j = i - (3 * k * k + k) // 2
      if j >= 0: s -= p[j] * (-1) ** k
      j = i - (3 * k * k - k) // 2
      if j >= 0: s -= p[j] * (-1) ** k
      k += 1
   p[i] = s % divisor
   if not p[i]:
      print i
      break
