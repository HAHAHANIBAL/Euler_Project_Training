#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc

import csv
import operator
import re
import CrawlWinners

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


#Only use 2010 and 2012 data for logit regression (2008 data is incomplete)
i=2012
#loop over the datasets I got and integrate all the senate candidate in one file
#while i < 2011:



winners=CrawlWinners.crawl(i)
#print len(winners)
path='CandidateSummaryAction %d.csv' %i
    #print path

fou=open('Candidate_Integrate.csv','wb')
writer=csv.writer(fou)

with open(path,'rb') as fin:
    fin.next()
    reader=csv.reader(fin)
    for row in reader:
        #collecting only candidates sought S, H or P position
        if row[1][:1]=='S':
            win_bool=0
            #some simple attributes with less objects can be quantified using logic gate
            if row[7]=='OPEN':
                row[7]=1
            elif row[7]=='CHALLENGER':
                row[7]=2
            #Incumbent is 3
            else:
                row[7]=3
            # I realized this is kind of not needed...since R can convert factor very quick
            if row[6]=='DEM':
                row[6]=1
            elif row[6]=='REP':
                row[6]=2
            else:
                row[6]=3
            #clean up the data, excel csv is just painful convert...
            if str(row[19])=='':
                row[19]=0
            if str(row[28])=='':
                row[28]=0
            if str(row[35])=='':
                row[35]=0
            if str(row[41])=='':
                row[41]=0
            if str(row[44])=='':
                row[44]=0
            if str(row[45])=='':
                row[45]=0
            #indexing the win/lose bool of the candidates, some candidates
            #cannot match due to inconsistency of names (Tom/Thomas, etc.)
            for item in winners:
                if item in row[2]:
                    win_bool=1
            #indexing the state as codes instead of abbreviations
            row[4]=candidate.states[row[4]]
            candidate.names[row[2]]=row[1]
            candidate.district[row[2]]=row[4]
            #print row[4]
            #I only selected some columns that I think is important for the prediction..kinda hurry and no time to improve the efficiency of the code..
            writer.writerow([win_bool,row[1],row[2],row[5],row[6],row[7],
                             str(row[19]).strip("$").replace(",",""),str(row[28]).strip("$").replace(",",""),str(row[35]).strip("$").replace(",",""),
                             str(row[41]).strip("$").replace(",",""),str(row[44]).strip("$").replace(",",""),str(row[45]).strip("$").replace(",","")])


name_pat=re.compile(r'(.*?),')

fou=open('Candidate_Individual_Expense.csv','wb')
writer=csv.writer(fou)

path='independent-expenditure %d.csv' %i
with open(path,'rb') as fin:
    fin.next()
    reader=csv.reader(fin)
    for row in reader:
        if row[0]==' ': #and row[5]!=' '
            #row[5]=candidate.states[row[5]]
            if name_pat.search(row[1])!=None:
                #print str(name_pat.search(row[1]).group()).strip('\,').upper()
                for key in candidate.names:
                    #matchup the candidate records from candidate summary to independent expenditure
                    if str(name_pat.search(row[1]).group()).strip('\,').upper() in key and row[5]==candidate.district[key]:
                        row[0]=candidate.names[key]
        #Output only corresponding data for the previous summary part
        #output only the reported numbers larger than $1, ignore some irregular data (wrong last name, short last names)
        if row[0]!=' ' and list(row[0])[0]=='S' and float(row[9].strip('$').replace(',',''))>1.00:
            writer.writerow([str(row[0]).upper(),row[1],row[9],row[12]])
            candidate.id[str(row[0]).upper()]=0

with open('Candidate_Individual_Expense.csv','rb') as fin:
    #skip the header
    reader=csv.reader(fin)
    #sum up all the expenses by their id
    for row in reader:
        try:
            candidate.id[row[0]]+=float(row[2].strip('$').replace(',',''))
        except Exception:
            continue
#print len(candidate.id)


fou=open('dat_output.csv','wb')
writer=csv.writer(fou,delimiter=',')
path='Candidate_Integrate.csv'
with open(path,'r') as fin:
    reader=csv.reader(fin)
    for row in reader:
        try:
            writer.writerow([row[0],row[2],row[3],row[4],row[5],row[6],
                             row[7],row[8],row[9],row[10],row[11],candidate.id[row[1]]])
        except Exception:
            writer.writerow([row[0],row[2],row[3],row[4],row[5],row[6],
                             row[7],row[8],row[9],row[10],row[11],0])

#print candidate.names

