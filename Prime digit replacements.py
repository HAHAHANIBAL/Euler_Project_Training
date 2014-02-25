#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #51

from sympy import isprime

#only repeating digits of 3 can be considered to be viable candidates for family size of primes larger than 8
#and the repeating digits can't be the last digit because the last digit has to be 1,3,7,9 as prime
#define dictionary to store the patterns in 5 digits,
#1 represents non-repeating digits, 0 represents repeating digits


def get5digits():
    digit={}
    digit[0]=[1,0,0,0,1]
    digit[1]=[0,1,0,0,1]
    digit[2]=[0,0,1,0,1]
    digit[3]=[0,0,0,1,1]
    return digit


def get6digits():
    digit={}
    digit[0]=[1,1,0,0,0,1]
    digit[1]=[1,0,1,0,0,1]
    digit[2]=[1,0,0,1,0,1]
    digit[3]=[1,0,0,0,1,1]
    digit[4]=[0,1,1,0,0,1]
    digit[5]=[0,1,0,1,0,1]
    digit[6]=[0,1,0,0,1,1]
    digit[7]=[0,0,1,1,0,1]
    digit[8]=[0,0,1,0,1,1]
    digit[9]=[0,0,0,1,1,1]
    return digit

#create an prototype pattern array for non-repeating number insertion
def fillnonrepeating(pat,number):
    nonrepeat=[0]*len(pat)
    temp=number
    for i in xrange(len(nonrepeat)-1,-1,-1):
        if pat[i]==1:
            nonrepeat[i]=temp%10
            temp/=10
        else:
            nonrepeat[i]=-1
    return nonrepeat

#cat the array intoa number with repeating number insertion
def catnumber(nonrepeat,repeatnum):
    temp=0
    for i in range(0,len(nonrepeat)):
        temp=temp*10
        #we can do this in str/int conversion or pure math way
        if nonrepeat[i]==-1:
            temp+=repeatnum
        else:
            temp+=nonrepeat[i]
    return temp

#calculate the total prime family size within on specific pattern
def familysize(repeatnum,pat):
    family_size=1
    n=repeatnum+1
    for i in range(n,10):
        if isprime(catnumber(pat,i)):
            family_size+=1
    return family_size


five=get5digits()
six=get6digits()
result=0
candidates=[]


for i in xrange(11,1000,2):
    if i%5==0:
        continue
    if i<100:
        pat=five
    else:
        pat=six
    for j in range(0,len(pat)):
        for k in range(0,3):
            if pat[j][0]==0 and k==0:
                continue
            proto=fillnonrepeating(pat[j],i)
            candidate=catnumber(proto,k)

            if isprime(candidate):
                candidates.append(candidate)
                if familysize(k,proto)==8:
                    result=candidate
                break

print result
