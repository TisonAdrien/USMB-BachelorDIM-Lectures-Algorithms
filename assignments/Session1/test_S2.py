# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 09:56:54 2017

@author: tisonad
"""

import S1_algotools as S
import numpy
import math
import pytest as p

def test_average_above_zero_result_5():
    tab = [7,7,7,0,3,0,3,3]
    res = S.average_above_zero(tab)
    assert res == 5

def test_average_above_zero_result_nan():
    tab = [-1,-10,-5,0,-8,0,-31,-12]
    res = S.average_above_zero(tab)
    assert math.isnan(res)

def test_average_above_zero_result_nan_withChar():
    tab = ['a','ab']
    res = S.average_above_zero(tab)
    assert math.isnan(res) 
   
def test_max_value_result_56():
    tab = [1,50,23,56,9,0]
    res = S.max_value(tab)
    assert res == 56

def test_max_value_result_5():
    tab = ['b',-100,5,2,-5,-45,'a']
    res = S.max_value(tab)
    assert res == 5

def test_max_value_result_error():
    tab = ['a','ac']
    with p.raises(Exception):
        S.max_value(tab)

def test_reverse_table_pair():
    tab = [1,2,'a',3,4,'b',5,6,'c']
    res = S.reverse_table(tab)
    assert res == ['c',6,5,'b',4,3,'a',2,1]

def test_reverse_table_impair():
    tab = [1,2,'a',3,4,'b',5,6]
    res = S.reverse_table(tab)
    assert res == [6,5,'b',4,3,'a',2,1]
    
def test_reverse_table_empty():
    tab = []
    with p.raises(Exception):
        S.reverse_table(tab)

def test_roi_bbox():
    mat = numpy.zeros([5,10])
    mat[2:4,5:9]=numpy.ones([2,4])
    res = S.roi_bbox(mat)
    assert res.all() == numpy.array([[2,5],[2,8],[3,5],[3,8]]).all()

def test_roi_bbox_empty():
    mat = numpy.zeros([5,10])
    res = S.roi_bbox(mat)
    assert res.all() == numpy.array([[0,0],[0,0],[0,0],[0,0]]).all()

def test_remove_whitespace_helloWorld():
    chaine = "Hello world ! "
    res = S.remove_whitespace(chaine)
    assert res == "Helloworld!"

def test_remove_whitespace_withoutSpace():
    chaine = "noSpace"
    res = S.remove_whitespace(chaine)
    assert res == "noSpace"
 
def test_remove_whitespace_empty():
    chaine = ""
    with p.raises(Exception):
        S.remove_whitespace(chaine)

def test_remove_whitespace_number():
    chaine = 5
    with p.raises(Exception):
        S.remove_whitespace(chaine)
        
def test_shuffle():
    tab = [1,2,3,4,5,6,7,8]
    res = S.shuffle(tab)
    assert sum(res) == sum(tab)

def test_shuffle_errorType():
    tab = "Hello world"
    with p.raises(Exception):
        S.shuffle(tab)

def test_shuffle_empty():
    tab = []
    with p.raises(Exception):
        S.shuffle(tab)

def test_sort_selective():
    tab = [5,1,26,5,8,9,3]
    res = S.sort_selective(tab)
    assert res == [1,3,5,5,8,9,26]

def test_sort_selective_empty():
    tab = []
    with p.raises(Exception):
        S.sort_selective(tab)

def test_sort_bubble():
    tab = [5,1,26,5,8,9,3]
    res = S.sort_bubble(tab)
    assert res == [1,3,5,5,8,9,26]

def test_sort_bubble_empty():
    tab = []
    with p.raises(Exception):
        S.sort_bubble(tab)
    
def test_random_fill_sparse_result_5():
    charMat = numpy.zeros([5,5],dtype=str)
    res = S.random_fill_sparse(charMat,5)
    assert (res == 'X').sum() == 5
    