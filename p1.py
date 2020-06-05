# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:38:15 2020

@author: Prakhyath Jain
"""

import sys

#task3 to print NaN for invalid input
try:
    curr=float(input('Enter Currency:'))
except:
    print('NaN')
    sys.exit()

#task2 round to two decimal places 
curr=format(curr,".2f")

curr=curr.split('.')

currency=list(curr[0])

#task1 to append $  at the first
if(currency[0]=='-'):
    currency.insert(1,'$')
else:
    currency.insert(0,'$')

k=0
i=len(currency)-1

while(i>=0):
    k+=1
    if(currency[i-1]=='$'):
        break
    if((k%3==0)):
        currency.insert(i,',')
    i-=1

for i in range(len(currency)):
    print(currency[i],end="")

print('.',end="")

print(curr[1])