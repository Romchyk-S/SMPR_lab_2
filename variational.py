# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:57:05 2022

@author: romas
"""

import sympy as sp

import numpy as np

def variational_method(Bayes_val, p_arr, eff_arr):
    
    max_Bayes = max(Bayes_val)
    
    ind = Bayes_val.index(max_Bayes)
    
    # print(ind)
    
    
    diff = []
    
    i = 0
    
    while i < len(Bayes_val):
        
        if i != ind:
            
            diff.append(max_Bayes - Bayes_val[i])
        
        i += 1
        
    print(diff)
    
    # для комбінацій 0,1; 0,2; 2,1
    
    q_1, q_2, q_3 = sp.symbols("q_1, q_2, q_3")
    
    variations_arr = [q_1, q_2, q_3]
    
    build_border_between_sets(0, 1, eff_arr, p_arr, diff[0],  variations_arr)
    
    print()
    
    build_border_between_sets(0, 2, eff_arr, p_arr, diff[1],  variations_arr)
    
    print()
    
    build_border_between_sets(1, 2, eff_arr, p_arr, diff[2],  variations_arr)
    
    
    
    return 0

def build_border_between_sets(set_1, set_2, eff_arr, p_arr, delta, var_arr):
    
    d = []
    
    i = 0
        
    while i < len(eff_arr):
        
        d.append(eff_arr[i][set_1] - eff_arr[i][set_2])
    
        i += 1
    
    p_var_arr = []
    
    i = 0
    
    while i < len(p_arr):
        
        p_var_arr.append(p_arr[i]+var_arr[i])
        
        i += 1
        
        
    dot_prod = (np.dot(d, var_arr))
        
    print(p_var_arr)
    
    print(dot_prod)
    
    
    # тут буде система dot_prod = delta, q_... = 0, q_1+q_2+q_3 = 0
    
    