#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

import re
import urllib2




def crawl(year):
    MainUrl='http://en.wikipedia.org/wiki/United_States_Senate_elections,_%d' %year
    req=urllib2.Request(MainUrl)
    resp=urllib2.urlopen(req)
    respHtml=resp.read()
    winner_pat=re.compile(r'(\w+).(\w+)</a></b>.*?\d+.*<br./>')
    i=winner_pat.findall(respHtml)

    winner=list((y.upper()+', '+x.upper()) for x, y in i)
    return winner



