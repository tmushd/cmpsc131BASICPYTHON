'''
Full Name:Vayunandanreddy Pannala
ID:9076422586
Date:23/03/2023
Filename:L5new.py
Purpose:assignment
'''

def avg_row(l1):
    for i in range(len(l1)):
        a=0
        for j in range(len(l1[i])):
            a+=l1[i][j]
        avg=a/len(l1[i])
        l1[i]+=[avg]
    return l1

def add_col(l2):
    lst=[0]*len(l2[0]) 
    for r in range(len(l2)):
        for c in range(len(l2[0])):
            lst[col]+=l2[r][c]
        
    return lst
def read_datafile(filepath):
    f= open(filepath,'r')
    a=f.readline()
    a=f.readline()
    result=[]
    while a!='':
        
        l=a.split()
        for i in range(len(l)):
            l[i]=float(l[i])
        result+=[l]
        a=f.readline()
    return result
def avg_col(l3):
    a=[0]*len(l3[0]) 
    for r in range(len(l3)):
        for c in range(len(l3[0])):
            a[col]+=l3[r][c]
    for i in range(len(a)):
        a[i] = a[i] / len(l3)
    l3+=[a]
    return l3


    
    
def main():
    print(avg_row([[1, 2, 3],[4, 5, 9],[1, 8, 9]]))
    print(add_col([[2, 2, 3],[4, 1, 9],[1, 1, 9]]))
    print(read_datafile("C:\Users\reddy\Downloads\L5 assignmentnew.txt"))
    print(avg_col(([ [1, 2, 3],[4, 5, 9],[1, 8, 9] ])))
    
if __name__ == '__main__':
    main()

  
    
  
