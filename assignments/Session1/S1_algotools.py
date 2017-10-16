# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 09:47:29 2017

@author: Adrien Tison, IUT Annecy : LPDIM
@brief a set of generic functions for data management

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
    if(nmax > 0):
        for i in xrange(nmax):
            if(type(table[i]) is float or type(table[i]) is int):
                if table[i]>0:
                    som = som + table[i]
                    n = n+1
                elif table[i]==0:
                    print('Zéro !')
                else:
                    print('Négatif : '+str(table[i]))
    if(n == 0):
        moy = float('nan')
    else:
        moy = float(som)/float(n)
    return moy
    
#random
import random

#tab = []

#append 200 random numbers in the list
#for i in xrange(200):
    #take a random integer between -100 and 100
#    rand = random.randint(-100,100)
    #append the random integer into te list
#    tab.append(rand)

#Call the function average_above_zero
#average = average_above_zero(tab)
#format the message to print
#message = "Average of random : {result}".format(result = average)
#print the message formated
#print(message)


## Second exercice
import math

def max_value(table):
    ##
    #basic function able to return the max value of a list
    #@param input list : a list to analyze
    #@throws an exception (ValueError) on an empty list
    #first check if provided list is not empty
    if len(table) == 0:
        #Exception
        raise Exception('Provided list is empty')
     
    #init max value
    nmax = len(table)
    max_find = False
    max_value = float('nan')
    for i in xrange(nmax):
        if(isinstance(table[i], float) or isinstance(table[i], int)):
            if(max_find == False):
                max_value = table[i]
                max_find = True
            if table[i]>max_value:
                max_value=table[i]
    if(math.isnan(max_value) == False):
        return max_value
    else:
        raise Exception('Provided list must have number')

#test max value function
#max_val = max_value(tab)
#message = "Max value is {result}".format(result=max_val)
#print(message)


## Third exercice

def reverse_table(table):
    ##
    #basic function able to return the reverse table
    #@param input list : a list to reverse
    #@throws an exception (ValueError) on an empty list
    #first check if provided list is not empty
    if len(table) == 0:
        #Exception
        raise Exception('Provided list is empty')
    
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
#print(reverse_table([1,2,3,4,5,6]))
#print(reverse_table([1,2,3,4,5,6,7]))        


##Fourth exercice
#matrix processing lib
import numpy
#Create an empty matrix 10x10
#myMat = numpy.zeros([5,10])
#set a value in a specific cell
#myMat[1,1] = 1
#set a value in a interval of the matrix
#myMat[2:4,5:9]=numpy.ones([2,4])
      
#print(myMat)

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
#print(roi_bbox(myMat))

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
#myCharMat = numpy.zeros([5,5],dtype=str)
#print(random_fill_sparse(myCharMat,5))



##Sixth exercice
def remove_whitespace(string):
    if(isinstance(string,basestring)):
        raise Exception('Provided string is not a string')
    lenght = len(string)
    if lenght == 0:
        #Exception
        raise Exception('Provided string is empty')
    i = 0
    while i<lenght:
        if string[i] == ' ':
            string = string[0:i] + string[i+1:len(string)]
            lenght-=1
        i+=1
    return string

#test function remove whitspace
# string = "Hello World 1 2 3"
# print(string+' => '+remove_whitespace(string))


##Seventh exercice
def shuffle(liste):
    ##
    # function to shuffle a list of values
    # @param list : the list of values to shuffle
    if len(liste) == 0:
        #Exception
        raise Exception('Provided list is empty')
    if(isinstance(liste, (list, tuple)) ):
        raise Exception('Provided list is not a list')
    second_list = liste[:]
    new_list = []
    length = len(second_list)
    for x in range(length):
        i = random.randint(0, len(second_list) - 1)
        new_list.append(second_list[i])
        del second_list[i]

    return new_list

#test function shuffle
#liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(liste)
#liste = shuffle(liste)
#print(liste)



##Eighth exercice
"""
Selective Sort
a)
[10, 15, 7, 1, 3, 3, 9]
min = 1, switch 10 and 1, restart with i=1
[1, 15, 7, 10, 3, 3, 9]
min = 3, switch 15 and 3, restart with i=2
[1, 3, 7, 10, 15, 3, 9]
min = 3, switch 7 and 3, restart with i=3
[1, 3, 3, 10, 15, 7, 9]
min = 7, switch 10 and 7, restart with i=4
[1, 3, 3, 7, 15, 10, 9]
min = 9, switch 15 and 9, restart with i=5
[1, 3, 3, 7, 9, 10, 15]

b) No, it depend of the length
c) length - 1, here : 6
d) 5
e) 7 * (7-1)/2 = 21
f) O(n^2)
g)  50 : 49 permutations, 1225 comparisons
    100 : 99 permutations, 4950 comparisons
    500 : 499 permutations, 124750 comparisons
"""

def sort_selective(liste):
    ##
    # function to sort a list
    # @param list to sort
    if len(liste) == 0:
        #Exception
        raise Exception('Provided list is empty')
    if(isinstance(liste, (list, tuple)) ):
        raise Exception('Provided list is not a list')
    for i in xrange(len(liste) - 1):
        min = i
        for x in xrange(i, len(liste)):
            if liste[x] < liste[min]:
                min = x

        if min != i:
            value = liste[min]
            liste[min] = liste[i]
            liste[i] = value

    return list

#test function sort_selective
#list = [10, 15, 7, 1, 3, 3, 9]
#print(list)
#list = sort_selective(list)
#print(list)


"""
Bubble Sort
a) 
[10, 15, 7, 1, 3, 3, 9]
switch 15 and 7
[10, 7, 15, 1, 3, 3, 9]
switch 15 and 1
[10, 7, 1, 15, 3, 3, 9]
switch 15 and 3
[10, 7, 1, 3, 15, 3, 9]
switch 15 and 3
[10, 7, 1, 3, 3, 15, 9]
switch 15 and 9
[10, 7, 1, 3, 3, 9, 15]
Restart
switch 10 and 7
[7, 10, 1, 3, 3, 9, 15]
switch 10 and 1
[7, 1, 10, 3, 3, 9, 15]
switch 10 and 3
[7, 1, 3, 10, 3, 9, 15]
switch 10 and 3
[7, 1, 3, 3, 10, 9, 15]
switch 10 and 9
[7, 1, 3, 3, 9, 10, 15]
Restart
switch 7 and 1
[1, 7, 3, 3, 9, 10, 15]
switch 7 and 3
[1, 3, 7, 3, 9, 10, 15]
switch 7 and 3
[1, 3, 3, 7, 9, 10, 15]
Sorted
b) Yes
c) 3
d) 13
e) 21
f) O(n^2)
g)  50 : 1175 permutations, 1225 comparisons
    100 : 4850 permutations, 4950 comparisons
    500 : 124250 permutations, 124750 comparisons
"""


def sort_bubble(liste):
    ##
    # function to sort a list
    # @param list to sort
    if len(liste) == 0:
        #Exception
        raise Exception('Provided list is empty')
    if(isinstance(liste, (list, tuple)) ):
        raise Exception('Provided list is not a list')
    for i in xrange(0, len(liste) - 1):
        for x in xrange(0, len(liste) - 1):
            if list[x] > list[x + 1]:
                value = list[x + 1]
                liste[x + 1] = liste[x]
                liste[x] = value

    return list


#test function sort_bubble
#list = [10, 15, 7, 1, 3, 3, 9]
#print(list)
#list = sort_bubble(list)
#print(list)
