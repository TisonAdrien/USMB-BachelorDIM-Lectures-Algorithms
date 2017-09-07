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
    ##
    #basic function able to return the average above zero of a list
    #@param input list : a list to analyze
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


def max_value(table):
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
max_val = max_value(tab)
message = "Max value is {result}".format(result=max_val)
print(message)


## Third exercice

def reverse_table(table):
    ##
    #basic function able to return the reverse table
    #@param input list : a list to reverse
    #@throws an exception (ValueError) on an empty list
    #first check if provided list is not empty
    if len(table) == 0:
        #Exception
        raise ValueError('Provided list is empty')
    
    pos_last = len(table)
    for i in xrange(len(table)/2):
        #second position to exchange
        pos_last-=1
        #process the exchange : take the first val, replace the first then replace the last value
        first = table[i]
        table[i] = table[pos_last]
        table[pos_last] = first
    return table

#Test reverse table function
print(reverse_table([1,2,3,4,5,6]))
print(reverse_table([1,2,3,4,5,6,7]))        


##Fourth exercice
#matrix processing lib
import numpy
#Create an empty matrix 10x10
myMat = numpy.zeros([5,10])
#set a value in a specific cell
#myMat[1,1] = 1
#set a value in a interval of the matrix
myMat[2:4,5:9]=numpy.ones([2,4])
      
print(myMat)

def roi_bbox(image):
    ##
    #function to bound an image with a binary code
    #@param matrix
    #output coordinates matrix
    min_y = image.shape[0]
    max_y = 0
    min_x = image.shape[1]
    max_x = 0
    index_of_y = 0
    for y in image:
        index_of_x = 0
        for x in y:
            if x == 1:
                if index_of_y < min_y:
                    min_y = index_of_y
                if index_of_y > max_y:
                    max_y = index_of_y
                if index_of_x < min_x:
                    min_x = index_of_x
                if index_of_x > max_x:
                    max_x = index_of_x
            index_of_x+=1
        index_of_y+=1
    
    bbox_coords = numpy.zeros([4,2],int)
    bbox_coords[0] = [min_y,min_x]
    bbox_coords[1] = [min_y,max_x]
    bbox_coords[2] = [max_y,min_x]
    bbox_coords[3] = [max_y,max_x]
    return bbox_coords
    
#test roi_bbox function
print(roi_bbox(myMat))

##Fifth exercice

def random_fill_sparse(table,vfill):
    ##
    #function to fill cells with value 'X'
    #@param matrix, vfill
    #output matrix
    for i in range(vfill):
        #take 2 randoms numbers
        y = random.randint(0,table.shape[0]-1)
        x = random.randint(0,table.shape[1]-1)
        #Check if 'X' is already write here
        while table[y,x] == 'X':
            y = random.randint(0,table.shape[0]-1)
            x = random.randint(0,table.shape[1]-1)
        table[y,x] = 'X'
    return table

#test function random_fill_sprase
myCharMat = numpy.zeros([5,5],dtype=str)
print(random_fill_sparse(myCharMat,5))



##Sixth exercice
def remove_whitespace(string):
    lenght = len(string)
    i = 0
    while i<lenght:
        if string[i] == ' ':
            string = string[0:i] + string[i+1:len(string)]
            lenght-=1
        i+=1
    return string

#test function remove whitspace
string = "Hello World 1 2 3"
print(string+' => '+remove_whitespace(string))


##Seventh exercice






