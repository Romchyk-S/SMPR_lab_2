# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:29:22 2022

@author: romas
"""

import re as re


def geom_method(Bayes_val):
    
    coefficients = get_coefs(Bayes_val)
    
    equations = get_equations(coefficients)
    
    points = get_points(equations)
    
    print(points)
    
    #побудувати графік
  
    return 0

def get_coefs(Bayes_val):
      
    coefs = []

    i = 0

    while i < len(Bayes_val):
        
        j = i+1
        
        while j < len(Bayes_val):
            
            difference = str(Bayes_val[i]-Bayes_val[j])
            
            coefs.append(re.split(r"[*]?p_\d", difference))
            
            j += 1
        
        i += 1
        
    return coefs
                

def get_equations(coefs):
    
    equations = []

    i = 0

    while i < len(coefs):
        
        change_coefs(coefs[i])
        
        equations.append(build_equations(coefs[i]))
        
        i += 1
        
    return equations

def change_coefs(coefs):
    
    j = 0
    
    while j < len(coefs):
        
        coefs[j] = coefs[j].replace(" ", "").replace("+", "")
        
        if j == 0 or j == 2:
            
            if re.match("\d", coefs[j]):
                
                coefs[j] = "-" + coefs[j]
                
            elif re.match("-\d", coefs[j]):
                
                coefs[j] = coefs[j].replace("-", "")
                
        if len(coefs[j]) == 0:
            
            coefs[j] = "1"
        
        j += 1
        
def build_equations(coefs):

    k = 0
    
    while k < len(coefs):
        
        coefs[k] = int(coefs[k])
        
        k += 1    
        
    if coefs[1] != "1":
        
        k = 0
        
        coef_p_2 = int(coefs[1])
        
        while k < len(coefs):
            
            coefs[k] = round(int(coefs[k]) / coef_p_2, 2)
            
            k += 1
            
    if coefs[2] > 0:
            
        return f"p_2 = {coefs[0]}*p_1 + {coefs[2]}"
        
    elif coefs[2] < 0:
        
        return f"p_2 = {coefs[0]}*p_1 {coefs[2]}"
        
    else:
        
        return f"p_2 = {coefs[0]}*p_1"
        
def get_points(equs):
    
    points = []

    i = 0

    while i < len(equs):
        
        point_i = []
        
        j = 0
        
        for_point_calc = equs[i].replace("p_2 = ", "").split("*p_1 ")
        
        while j < len(for_point_calc):
            
            for_point_calc[j] = float(for_point_calc[j].replace(" ", ""))
            
            j += 1

        
        k = 0
        
        while k < 2:
            
            point_i.append((k, round(for_point_calc[0]*k+for_point_calc[1],2)))
            
            k += 1
            
        points.append(point_i)
            
        i += 1
        
    return points