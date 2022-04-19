# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:40:50 2022

@author: romas
"""

def get_bayes_values(p_arr, eff_arr):
    
    Bayes_val = []

    i = 0

    while i < len(eff_arr[0]):
        
        res = 0
        
        j = 0
        
        while j < len(eff_arr):
            
            res += eff_arr[j][i] * p_arr[j]
            
            if type(res) == float:
                
                res = round(res, 2)
            
            j += 1
        
        Bayes_val.append(res)
            
        i += 1
        
    return Bayes_val