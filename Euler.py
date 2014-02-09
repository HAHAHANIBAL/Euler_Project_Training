#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

from pylab import *


sum=0

#Euler #1
for i in range(0,1001):
    if i%3==0 or i%5==0:
        sum+=i


print sum

#Euler #2
i=1
j=2
fib=0
sum=0

while fib<4000000:
    fib=i+j
    if fib%2==0:
        sum+=fib
    i=j
    j=fib


print sum+2

#Euler #3
n = 600851475143
i = 2
#a number can only have one prime factor whose value is larger than sqrt(n)
while i*i<n:
     while n%i == 0:
         n=n/i
     i=i+1

print n

#Euler #4
i=9
for j in range(0,10):
    for k in range(0,10):
        number=int(str(i)+str(j)+str(k)+str(k)+str(j)+str(i))
        for count in range(900,999):
            if number/count<1000 and number%count==0:
                print number

#Euler #5
i=0
#all prime factors
n=3*5*7*11*13*17*19
count=0
while i!=1:
    for j in range(2,21):
        count+=n%j
    if count==0:
        i=1
    n=n*3*2
    count=0

count=0
#delete additional 3s and 2s
n=n/3/3/3/3/2
for j in range(2,21):
    count+=n%j
print n

#Euler #6
sum1=0
sum2=0
for i in range(1,101):
    sum2+=i
    sum1+=i*i

print sum2*sum2-sum1

#Euler #7
n=1
count=0
i=0
flg=0
while i!=1:
    n+=2
    if n%2!=0 and n%3!=0 and n%5!=0 and sqrt(n)%1!=0:
        for j in range(7,int(sqrt(n))+1):
            if n%j==0:
                flg+=1
        if flg==0:
            count+=1
    if count+3==10001:
        i=1
    flg=0

print n

#Euler #8
number='7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
max=0
a=0
for i in range(0,996):
    a=int(number[i])*int(number[i+1])*int(number[i+2])*int(number[i+3])*int(number[i+4])
    if a>max:
        max=a
print max

#Euler #9
for i in range(1,501):
    for j in range(1,501):
        if i*i+j*j==(1000-i-j)*(1000-i-j):
            print i*j*(1000-i-j)

#Euler #10
n=1
sum=0
i=0
flg=0
while i!=1:
    n+=2
    if n%2!=0 and n%3!=0 and n%5!=0 and sqrt(n)%1!=0:
        for j in range(7,int(sqrt(n))+1):
            if n%j==0:
                flg+=1
        if flg==0:
            sum+=n
    if n>2000000:
        i=1
    flg=0

print sum
