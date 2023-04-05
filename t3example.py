# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:28:10 2023

@author: rpp5501"""

def find_number(fname,x):
    
    a= open(fname,'r')
    l= a.readline()
    lst_2d_str=[]
    lst_2d_int=[]
    #initializing variables; a is the variable which stores the file, l contains each line of the file.
    
    
    while l!='':
        lst_2d_str+=[l.split()]
        l=a.readline()
    print(lst_2d_str)
    #stores the given file fname in the two dimensional list and converts it to a printable form.
    
    lst_2d_int1=[]
    for i in range(len(lst_2d_str)):
        row=[0]*len(lst_2d_str[0])
        lst_2d_int1+=[row]
    #makes a new list lst_2d_int1 of the same size as lst_2d_str and assigns all elements to 0
    
        
     for i in range(len(lst_2d_str)):
        for j in range(len(lst_2d_str[i])):
            lst_2d_int1[i][j]=int(lst_2d_str[i][j])
            if lst_2d_int1[i][j]<x:
                 lst_2d_int+=[lst_2d_int1[i][j]]               
    print(lst_2d_int1,'lst_2d_int',lst_2d_int)
    #prints all values in the list that is less than the integer x
    
    
    
    min_val=9999999999999
    for i in range(len(lst_2d_int1)):
        for j in range(len(lst_2d_int1[i])):
            if lst_2d_int1[i][j]<min_val:
                min_val=lst_2d_int1[i][j]
    print(type(min_val), "min: ", min_val)
    #prints the minimum value of the list
                
    print(all(isinstance(x, int) for x in lst_2d_int))#prints everytime x is an element in the list
    return lst_2d_int#returns the integer list form of the given file.
