#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #79

import time


def problem79():

    digits_positions = {}

    with open('keylog.txt') as file:
        file_content = file.read()
        codes = file_content.split(sep='\n')
        digits = {str(d) for d in range(10) if str(d) in file_content}

    for d in digits:
        position = len({c
                        for code in codes if d in code
                        for c in code[:code.index(d)]})
        digits_positions[d] = position

    passcode = ''.join(sorted(digits_positions, key=digits_positions.get))
    return passcode

start = time.time()
print(problem79())
print('\nExecution time: {0} seconds'.format(time.time() - start))
