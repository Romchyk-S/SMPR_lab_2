# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:58:39 2022

@author: romas
"""

def get_data_from_file(file_name):
    
    p = []

    eff = []
    
    f = open(str(file_name))

    for s in f:
        
        s = s.strip().split(" ")
        
        arr = []
        
        i = 0
        
        while i < len(s):
            
            if i == 0:
                
                p.append(float(s[i]))
                
            else:
                
                arr.append(int(s[i]))
            
            i += 1
            
        eff.append(arr)
        
    return p, eff