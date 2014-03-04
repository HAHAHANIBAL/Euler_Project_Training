#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=mehmetbercan
#Euler #59

import itertools
import re

pat=re.compile(r'\d+')

with open('cipher1.txt','rb') as fin:
    for line in fin:
        match=pat.findall(line)



strcipher = str(bytearray(eval('[' + open('cipher1.txt').readlines()[0] + ']')))


def getkeyincipherlength(cipherlength, key):
    longkey=""
    while True:
        for k in key:
            longkey+=k
            if len(longkey)==cipherlength:
                return longkey


def encrypt(strcipher, key):
    longkey=getkeyincipherlength(len(strcipher), key)
    return str(bytearray([ord(strcipher[i])^ord(longkey[i]) for i in xrange(len(strcipher))]))

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

permutations_ = [e for e in itertools.permutations(alphabet, 3)]

for perm in permutations_:
    key=""
    for k in perm:
        key+=k
    txt = encrypt(strcipher, key)
    lowertxt=txt.lower()
    if " the " in lowertxt:
        print "Key: ", key
        print "Answer: ", sum([ord(txt[i]) for i in xrange(len(txt))])
        break
