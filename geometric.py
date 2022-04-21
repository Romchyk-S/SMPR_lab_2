# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:29:22 2022

@author: romas
"""

import re as re

import matplotlib.pyplot as plt

import prettytable as pt


def geom_method(Bayes_val, p_1, p_2):
    
    coefficients = get_coefs(Bayes_val, p_1, p_2)
    
    equations = get_equations(coefficients)
    
    print(equations)
    
    print()
    
    points = get_points(equations)
    
    print(points)
    
    print()
    
    legend_arr = plotting_lines(points)
    
    Bayes_values_table = pt.PrettyTable()
    
    Bayes_values_table.field_names = ["Координати", "B+(p, φ_1)", "B+(p, φ_2)", "B+(p, φ_3)", "Максимальне значення", "Баєсова множина"]
    
    # розбити графік на множини, обрати точки з кожної множини
    
    x = 0.4
    
    y = 0.4

    row = create_new_row(x, y, Bayes_val, p_1, p_2, points)
    
    Bayes_values_table.add_row(row)
    
    print(Bayes_values_table)
    
    plt.legend(legend_arr)
    
    plt.show()
    
    return 0

def get_coefs(Bayes_val, p_1, p_2):
      
    coefs = []

    i = 0

    while i < len(Bayes_val):
        
        j = i+1
        
        while j < len(Bayes_val):
            
            difference = Bayes_val[i]-Bayes_val[j]
            
            difference = str(difference)
            
            split_string = re.split(r"[*]?p_\d", difference)
            
            k = 0
            
            while k < len(split_string):
                
                temp_string = re.split(r"\s", split_string[k])
                
                t = 0
                
                while t < len(temp_string):
                    
                    if re.search("\D$", temp_string[t]):
                        
                        temp_string[t] += temp_string[t+1] 
                        
                        temp_string.remove(temp_string[t+1])
                        
                    t += 1
                
                if re.search("\D?\d", temp_string[0]) and len(temp_string) > 1:
                    
                    split_string[k] = temp_string[0]
                    
                    split_string[k+1] = temp_string[1]
                
                k += 1
            
            if len(split_string) < 3:
                
                if "p_1" not in str(difference):
                    
                    split_string.insert(0, '0')
                    
                if "p_2" not in str(difference):
                    
                    split_string.insert(1, '0')
                    
                if len(split_string) < 3:
                    
                    split_string.insert(2, '0')
                    
            if '' in split_string:
                
                ind = split_string.index('')
                
                split_string[ind] = '0'
                
            coefs.append(split_string)
            
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
            
            # вирішити проблему p_2 = 0
            
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
        
    points.append([(0, 1), (1, 0)])
        
    return points

def plotting_lines(points):
    
    count = 0
    
    arr = []
    
    plt.xlim([0,1])
    
    plt.ylim([0,1])
    
    for p in points:
        
        x_values = [p[0][0], p[1][0]]
        
        y_values = [p[0][1], p[1][1]]
        
        plt.fill_between([0,1], y_values, alpha=0.4)
        
        plt.plot(x_values, y_values)
        
        count += 1
        
        arr.append(count)
        
    # plt.show()
    
    return arr
    
def get_bayes_val_for_point(x, y, Bayes_val, p_1, p_2):
    
    point_Bayes_val = []
      
    for i in Bayes_val:
        
        i = i.replace(p_1, x).replace(p_2, y)
        
        point_Bayes_val.append(i)
        
    max_value = max(point_Bayes_val)
    
    max_ind = point_Bayes_val.index(max_value)
    
    Bayes_set = f"φ_{max_ind+1}"
    
    return point_Bayes_val, max_value, Bayes_set

def create_new_row(x, y, Bayes_val, p_1, p_2, points):
    
    row = []

    plt.scatter(x, y)
    
    row.append((x, y))
    
    point_Bayes_val, index, Bayes_set = get_bayes_val_for_point(x, y, Bayes_val, p_1, p_2)
    
    for i in point_Bayes_val:
        
        row.append(i)
        
    row.append(index)
    
    row.append(Bayes_set)
    
    return row