# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:28:10 2023

@author: rpp5501"""

def find_number(fname,x):
    a= open(fname,'r')
    l= a.readline()
    lst_2d_str=[]
    lst_2d_int=[]
    
    while l!='':
        lst_2d_str+=[l.split()]
        l=a.readline()
    print(lst_2d_str)
    lst_2d_int1=[]
    
    for i in range(len(lst_2d_str)):
        row=[0]*len(lst_2d_str[0])
        lst_2d_int1+=[row]
        
    for i in range(len(lst_2d_str)):
        for j in range(len(lst_2d_str[i])):
            lst_2d_int1[i][j]=int(lst_2d_str[i][j])
            if lst_2d_int1[i][j]<x:
                 lst_2d_int+=[lst_2d_int1[i][j]]
                    
    print(lst_2d_int1,'lst_2d_int',lst_2d_int)
    
    min_val=9999999999999
    
    for i in range(len(lst_2d_int1)):
        for j in range(len(lst_2d_int1[i])):
            if lst_2d_int1[i][j]<min_val:
                min_val=lst_2d_int1[i][j]
                
    print(type(min_val), "min: ", min_val)
    print(all(isinstance(x, int) for x in lst_2d_int))
    return lst_2d_int
