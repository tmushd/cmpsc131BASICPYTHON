'''
Full Name:Vayunandanreddy Pannala
ID:9076422586
Date:23/03/2023
Filename:L5new.py
Purpose:assignment
'''

def avg_row(lst):
    for i in range(len(lst)):
        a=0
        for j in range(len(lst[i])):
            a+=lst[i][j]
        avg=a/len(lst[i])
        lst[i]+=[avg]
    return lst

def add_col(lst):
    lst1=[0]*len(lst[0]) 
    for row in range(len(lst)):
        for col in range(len(lst[0])):
            lst1[col]+=lst[row][col]
        
    return lst1
def read_datafile(fpath):
    f= open(fpath,'r')
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
def avg_col(lst):
    lst1=[0]*len(lst[0]) 
    for row in range(len(lst)):
        for col in range(len(lst[0])):
            lst1[col]+=lst[row][col]
    for i in range(len(lst1)):
        lst1[i] = lst1[i] / len(lst)
    lst+=[lst1]
    return lst


    
    
def main():
    print(avg_row([[1, 2, 3],[4, 5, 9],[1, 8, 9]]))
    print(add_col([[2, 2, 3],[4, 1, 9],[1, 1, 9]]))
    print(read_datafile("C:\Users\reddy\Downloads\L5 assignmentnew.txt"))
    print(avg_col(([ [1, 2, 3],[4, 5, 9],[1, 8, 9] ])))
    
if __name__ == '__main__':
    main()

  
    
  
