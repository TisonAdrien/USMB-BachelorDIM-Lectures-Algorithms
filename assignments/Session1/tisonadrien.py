# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 09:47:29 2017

@author: Adrien Tison, IUT Annecy : LPDIM
@brief a set of generic functions for data management

#a empty list
tab = []
#a filled list
tab = [0,1,2,3,4,5,6,7,8,9]
#append to a list
tab.append(10)
#a buggy list
mybuggylist = [1,'a',"Hi"]

#a variable
a = 0 # default type : int

#operators
b=a+2
list_sum = tab+mybuggylist

"""

##  First exercice
    
#Declare a function with an input list return float
def average_above_zero(table):
    som = 0
    n = 0
    #nmax is the lenght of my list
    nmax = len(table)
    
    for i in xrange(nmax):
        if table[i]>0:
            som = som + table[i]
            n = n+1
        elif table[i]==0:
            print('Zéro !')
        else:
            #print('Négatif : '+str(table[i]))
            som = som + table[i]
            n = n+1
    moy = float(som)/float(n)
    return moy
    
#random
import random

tab = []

#append 200 random numbers in the list
for i in xrange(200):
    #take a random integer between -100 and 100
    rand = random.randint(-100,100)
    #append the random integer into te list
    tab.append(rand)

#Call the function average_above_zero
average = average_above_zero(tab)
#format the message to print
message = "Average of random : {result}".format(result = average)
#print the message formated
print(message)


## Second exercice


def max_value_of(table):
    ##
    #basic function able to return the max value of a list
    #@param input list : a list to analyze
    #@throws an exception (ValueError) on an empty list
    #first check if provided list is not empty
    if len(table) == 0:
        #Exception
        raise ValueError('Provided list is empty')
     
    #init max value
    max_value = table[0]
    nmax = len(table)
    for i in xrange(nmax):
        if table[i]>max_value:
            max_value=table[i]
    return max_value

#test max value function
max_val = max_value_of(tab)
message = "Max value is {result}".format(result=max_val)
print(message)




