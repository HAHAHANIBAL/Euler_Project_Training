#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #61

#def class
class Euler61:
    solution=[0]*6
    numbers={}

#recursive solution
def findnext(last,length):
    for i in range(0,len(Euler61.solution)):
        if Euler61.solution[i]!=0:
            continue
        for j in range(0,len(Euler61.numbers[i])):
            unique=True
            for k in range(0,len(Euler61.solution)):
                if Euler61.numbers[i][j]==Euler61.solution[k]:
                    unique=False
                    break
            if unique and Euler61.numbers[i][j]/100==Euler61.solution[last]%100:
                Euler61.solution[i]=Euler61.numbers[i][j]
                if length==5:
                    if Euler61.solution[5]/100==Euler61.solution[i]%100:
                        return True
                if findnext(i,length+1):
                    return True
        Euler61.solution[i]=0
    return False

#generate list of num
def gennum(types):
    numbers=[]
    n=0
    number=0

    while number<10000:
        n+=1
        if types==0:
            number=n*(n+1)/2
        elif types==1:
            number=n*n
        elif types==2:
            number=n*(3*n-1)/2
        elif types==3:
            number=n*(2*n-1)
        elif types==4:
            number=n*(5*n-3)/2
        elif types==5:
            number=n*(3*n-2)

        if number>999:
            numbers.append(number)

    return numbers[0:-1]


#main
for i in range(0,6):
    Euler61.numbers[i]=gennum(i)

for i in range(0,len(Euler61.numbers[5])):
    #define the last possible value
    Euler61.solution[5]=Euler61.numbers[5][i]
    #use recursive function to track back all possible numbers and see if they fit
    if findnext(5,1):
        break

result=sum(Euler61.solution)
print result