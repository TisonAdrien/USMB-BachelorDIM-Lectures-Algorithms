# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 09:56:54 2017

@author: tisonad
"""

import tisonadrien
import numpy

def test_average_above_zero_result_1():
    tab = [1,1,1,0,1,0,1,1]
    res = tisonadrien.average_above_zero(tab)
    assert res == 1

def test_average_above_zero_result_moins1():
    tab = [-1,-1,-1,0,-1,0,-1,-1]
    res = tisonadrien.average_above_zero(tab)
    assert res == 0
    
def test_max_value_result_56():
    tab = [1,50,23,56,9,0]
    res = tisonadrien.max_value(tab)
    assert res == 56

def test_max_value_result_5():
    tab = [-100,5,2,-5,-45,0]
    res = tisonadrien.max_value(tab)
    assert res == 5

def test_reverse_table_pair():
    tab = [1,2,3,4,5,6,7,8,9]
    res = tisonadrien.reverse_table(tab)
    assert res == [9,8,7,6,5,4,3,2,1]

def test_reverse_table_impair():
    tab = [1,2,3,4,5,6,7,8]
    res = tisonadrien.reverse_table(tab)
    assert res == [8,7,6,5,4,3,2,1]

def test_roi_bbox():
    mat = numpy.zeros([5,10])
    mat[2:4,5:9]=numpy.ones([2,4])
    res = tisonadrien.roi_bbox(mat)
    assert res.all() == numpy.array([[2,5],[2,8],[3,5],[3,8]]).all()
    
def test_remove_whitespace():
    chaine = "Hello world ! "
    res = tisonadrien.remove_whitespace(chaine)
    assert res == "Helloworld!"
    
def test_sort_selective():
    tab = [5,1,26,5,8,9,3]
    res = tisonadrien.sort_selective(tab)
    assert res == [1,3,5,5,8,9,26]

def test_sort_bubble():
    tab = [5,1,26,5,8,9,3]
    res = tisonadrien.sort_bubble(tab)
    assert res == [1,3,5,5,8,9,26]