#!/usr/bin/python
#-*- coding: utf-8 -*-

import csv
import operator
import re

#create a class to store some quantified attributes besides expenditure
class candidate:
    states={}
    individual_expense_support={}
    individual_expense_oppose={}
    disbursements={}
    names={}
    district={}
    id={}

with open('states.csv','rb') as fin:
    #skip the header
    fin.next()
    reader=csv.reader(fin)
    for row in reader:
        candidate.states[row[1]]=row[2]


#you can actually sort the dict here, but it's not necessary
#candidate.states=sorted(candidate.states.iteritems(),key=operator.itemgetter(1))
#print candidate.states
fou=open('Candidate_Integrate.csv','wb')
writer=csv.writer(fou,delimiter=',')

#individual expense and disbursement data don't have year 2008 though..
i=2010
#loop over the datasets I got and integrate all the senate candidate in one file
while i < 2015:
    path='CandidateSummaryAction %d.csv' %i
    #print path
    with open(path,'rb') as fin:
        fin.next()
        reader=csv.reader(fin)
        for row in reader:
            #some simple attributes with less objects can be quantified using logic gate
            if row[7]=='OPEN':
                row[7]=1
            elif row[7]=='CHALLENGER':
                row[7]=2
            else:
                row[7]=3
            #indexing the state as codes instead of abbreviations
            row[4]=candidate.states[row[4]]
            candidate.names[row[2]]=row[1]
            candidate.district[row[2]]=row[4]
            #print row[4]
            writer.writerow(row)
        i=i+2

name_pat=re.compile(r'(.*?),')

fou=open('Candidate_Individual_Expense.csv','wb')
writer=csv.writer(fou,delimiter=',')

path='independent-expenditure 2010.csv'
with open(path,'rb') as fin:
    fin.next()
    reader=csv.reader(fin)
    for row in reader:
        if row[0]==' ' and row[5]!=' ':
            row[5]=candidate.states[row[5]]
            if name_pat.search(row[1])!=None:
#                print str(name_pat.search(row[1]).group()).strip('\,').upper()
                for key in candidate.names:
                    if str(name_pat.search(row[1]).group()).strip('\,').upper() in key and row[5]==candidate.district[key]:
                        row[0]=candidate.names[key]
        if row[0]!=' ':
            writer.writerow([str(row[0]).upper(),row[1],row[11],row[12]])
            candidate.id[str(row[0]).upper()]=0

with open('Candidate_Individual_Expense.csv','rb') as fin:
    #skip the header
    reader=csv.reader(fin)
    for row in reader:
        candidate.id[row[0]]+=int(row[2])

print candidate.id


#print candidate.names

