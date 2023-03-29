Full Name:mayank futnani arupula
ID:951593459
Date:23/03/2023
Filename:L2_arupula_mayank_mxa6067.py
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
    lst1=[0]*len(l2[0]) 
    for row in range(len(l2)):
        for col in range(len(l2[0])):
            lst1[col]+=l2[row][col]
        
    return lst1
def read_datafile(fpath):
    f= open(fpath,'r')
    read_file=f.readline()
    read_file=f.readline()
    result=[]
    while read_file!='':
        
        l=read_file.split()
        for i in range(len(l)):
            l[i]=float(l[i])
        result+=[l]
        read_file=f.readline()
    return result
def avg_col(l4):#lst = l4
    lst1=[0]*len(l4[0]) 
    for row in range(len(l4)):
        for col in range(len(l4[0])):
            lst1[col]+=l4[row][col]
    for i in range(len(lst1)):
        lst1[i] = lst1[i] / len(l4)
    lst+=[lst1]
    return l4


    
    
def main():
    print(avg_row([[1, 2, 3],[4, 5, 9],[1, 8, 9]]))
    print(add_col([[2, 2, 3],[4, 1, 9],[1, 1, 9]]))
    print(read_datafile("C:\\Users\\mayank\\Documents\\file.txt"))
    print(avg_col(([ [1, 2, 3],[4, 5, 9],[1, 8, 9] ])))
    
if _name_ == '_main_':
    main()
