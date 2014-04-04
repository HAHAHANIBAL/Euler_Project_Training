#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #89

def integer(roman):
    numbers = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    values = [1000, 500, 100, 50, 10, 5, 1]
    places = []
    for i in range(len(roman)):
        value = values[numbers.index(roman[i])]
        try:
            next_value = values[numbers.index(roman[i + 1])]
            if next_value > value:
                value *= -1
        except IndexError:
            pass
        places.append(value)
    return sum(places)

def roman(integer):
    integers = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    numbers = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = ""
    for i in range(len(integers)):
        count = int(integer / integers[i])
        result += numbers[i] * count
        integer -= integers[i] * count
    return result

def main():
    count, romans = 0, open("roman.txt", 'r').read().split('\n')
    for r in romans:
        count += len(r) - len(roman(integer(r)))
    print count