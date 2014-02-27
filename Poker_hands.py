#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #54

player1='4H KC 2S 7S KD'
player2='KC KS 2S 8D 2D'
hands3='KC KS KS 1D 2D'
hands4='KC KS KS QD JD'
hands5='9C TC JC 3C 2C'
hands6='9C 9C 9C 9C 3C'
hands7='9C 9C 9C 3C 3C'
hands8='TC JC QC KC AC'


def def_rank(val):
    if ord(val)-65<0:
        return int(val)
    elif ord(val)-65==0:
        return 14
    elif ord(val)-84==0:
        return 10
    elif ord(val)-74==0:
        return 11
    elif ord(val)-81==0:
        return 12
    else:
        return 13

def judge_val(hands):
    temp=[]
    value=[]
    suit=[]
    for i in range(0,5):
        crt=i*3
        tmp_val=def_rank(hands[crt])
        if hands[crt+1] not in suit:
            suit.append(hands[crt+1])
        if tmp_val not in temp:
            temp.append(tmp_val)
        else:
            value.append(tmp_val)


    rank_suit=0
    if len(suit)==1:
        #flush
        if len(temp)!=5 or max(temp)-min(temp)!=4:
            rank_suit=5
            pair_val=max(temp)
        #straight flush
        elif len(temp)==5 and max(temp)-min(temp)==4 and max(temp)<14:
            rank_suit=8
            pair_val=max(temp)
        #royal flush
        else:
            rank_suit=9
            pair_val=max(temp)

    rank_num=0
    #one pair
    if len(temp)==4:
        rank_num=1
        pair_val=max(value)
    #two pairs
    elif len(temp)==3 and max(value)!=min(value):
        rank_num=2
        pair_val=max(value)+min(value)
    #three of a kind
    elif len(temp)==3 and max(value)==min(value):
        rank_num=3
        pair_val=max(value)
    #straight
    elif len(temp)==5 and max(temp)-min(temp)==4 and len(suit)>1:
        rank_num=4
        pair_val=max(temp)
    #four of a kind
    elif len(temp)==2 and max(value)-min(value)==0:
        rank_num=7
        pair_val=max(value)
    #three of a kind and a pair
    elif len(temp)==2 and max(value)-min(value)!=0:
        rank_num=6
        pair_val=max(value)+min(value)
    else:
        rank_num=0
        pair_val=max(temp)

    if rank_suit>rank_num:
        return rank_suit, pair_val, sorted(temp)
    else:
        return rank_num, pair_val, sorted(temp)




print judge_val(player1)
print judge_val(player2)
print judge_val(hands3)
print judge_val(hands4)
print judge_val(hands5)
print judge_val(hands6)
print judge_val(hands7)
print judge_val(hands8)


def compare_rank(val1,val2):
    flg=0
    i=0
    while flg==0:
        flg=val1[i]-val2[i]
        i+=1
    if flg<0:
        return 2
    if flg>0:
        return 1

dealt1=judge_val(hands3)
dealt2=judge_val(hands4)

print dealt1[2][0]