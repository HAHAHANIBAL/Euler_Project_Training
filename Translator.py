#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #17
import math


init_array=['zero','one','two','three','four','five','six','seven','eight','nine','ten',
            'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
ten_array=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

total_array=['']*1001
digit_length=0
for i in range(1,1001):
    number=i
    if number<20:
        total_array[number]=init_array[number]
        digit_length+=len(total_array[number])
    elif number>=20 and number%10==0 and number<100:
        total_array[number]=ten_array[(number/10-2)]
        digit_length+=len(total_array[number])
    elif number>20 and number%10!=0 and number<100:
        total_array[number]=ten_array[(number/10-2)]+init_array[number%10]
        digit_length+=len(total_array[number])
        #print len(ten_array[(number/10-2)]+init_array[number%10])
    elif number>=100 and number%100==0 and number<1000:
        total_array[number]=init_array[number/100]+'hundred'
        digit_length+=len(total_array[number])
        #print init_array[number/100]+'hundred'
    elif number>100 and number%100!=0 and number<1000:
        total_array[number]=total_array[number-number%100]+'and'+total_array[number%100]
        digit_length+=len(total_array[number])
    else:
        total_array[number]='onethousand'
        digit_length+=len(total_array[number])

print total_array[190]
print digit_length