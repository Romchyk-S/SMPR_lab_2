# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:57:05 2022

@author: romas
"""

import sympy as sp

import numpy as np

import re as re


def variational_method(Bayes_val, p_arr, eff_arr):
    
    
    diff = []
    
    i = 0
    
    while i < len(Bayes_val):
        
        j = i+1
        
        while j < len(Bayes_val):
            
            if Bayes_val[i] > Bayes_val[j]:
            
                diff.append(Bayes_val[i]-Bayes_val[j])
                
            else:
                
                diff.append(Bayes_val[j]-Bayes_val[i])
            
            j += 1
        
        i += 1
    
    q_1, q_2, q_3 = sp.symbols("q_1, q_2, q_3")
    
    variations_arr = [q_1, q_2, q_3]
    
    build_border_between_sets(0, 1, eff_arr, p_arr, diff[0],  variations_arr)
    
    print()
    
    build_border_between_sets(0, 2, eff_arr, p_arr, diff[1],  variations_arr)
    
    print()
    
    build_border_between_sets(1, 2, eff_arr, p_arr, diff[2],  variations_arr)

def build_border_between_sets(set_1, set_2, eff_arr, p_arr, delta, var_arr):
    
    d = []
    
    i = 0
        
    while i < len(eff_arr):
        
        d.append(eff_arr[i][set_1] - eff_arr[i][set_2])
    
        i += 1
        
    dot_prod = (np.dot(d, var_arr))

    points = get_points(dot_prod, delta, var_arr, p_arr)  
    
    get_border_equation(points)
   
    
def get_points(dot, delta, var_arr, p_arr):
    
    points = []
    
    i = 0
    
    while i < 2:
        
        res = sp.solve([sp.Eq(dot, delta), sp.Eq(var_arr[i], 0), sp.Eq(sum(var_arr), 0)])
        
        res_vals = list(res.values())
        
        j = 0
        
        point = []
        
        while j < len(p_arr):
            
            point.append(p_arr[j]+res_vals[j])
            
            j += 1
        
        points.append(point)
        
        i += 1
        
    return points

def get_border_equation(points):
    
     
    p_1, p_2 = sp.symbols("p_1, p_2")
    
    border_equation = [(points[1][1]-points[0][1])*(p_1-points[0][0]), ((p_2-points[0][1])*(points[1][0]-points[0][0]))]

    i = 0
    
    while i < len(border_equation):
        
        border_equation[i] = str(border_equation[i])
        
        if type(re.search(r"\Ap_\d", border_equation[i])) != None:
            
            border_equation[i] = re.sub(r"\Ap_", "1*p_", border_equation[i])
       
        border_equation[i] = re.sub(r"p_\d", r"", border_equation[i])

        
        border_equation[i] = re.split(r" ", border_equation[i])
        
        j = 0
        
        while j < len(border_equation[i]):
            
            if border_equation[i][j] == "+" or border_equation[i][j] == "-":
                
                border_equation[i][j] += border_equation[i][j+1]
                
                border_equation[i].remove(border_equation[i][j+1])
                
                break
            
            j += 1


        k = 0
        
        while k < len(border_equation[i]):
            
            if type(re.search(r"\*", border_equation[i][k])) == re.Match:
                
                border_equation[i].insert(0,  re.sub(r"\*", "", border_equation[i][k]))
                
                border_equation[i][k+1] = ""
                
                border_equation[i].remove(border_equation[i][k+1])
                
                break
            
            k += 1
        
        
        i += 1
    
    i = 0
    
    while i < len(border_equation):
        
        j = 0
        
        while j < len(border_equation[i]):
            
            border_equation[i][j] = float(border_equation[i][j])
            
            j += 1
        
        i += 1

    
    b = round((-border_equation[1][1] + border_equation[0][1]) / (border_equation[1][0]), 2)
    
    k = round((border_equation[0][0])/(border_equation[1][0]),2)
    
    if b > 0:
    
        print(f"p_2 = {k}*p_1 + {b}")
        
    elif b == 0:
        
        print(f"p_2 = {k}*p_1 + {b}")
        
    else:
        
        print(f"p_2 = {k}*p_1{b}")
        