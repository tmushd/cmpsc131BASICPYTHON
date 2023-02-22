import math
#range roller is basic output control
def range_roller(N,K):
    if K==0:
        for i in range(N,(2*N)+2,3):
            a = []
            a.append(i)
            return a
    elif K==1:
        for i in range(0,N+1,2):
            a = []
            a.append(i)
            a.reverse()
            return a
    else:
        i = -1
        return i
#while_it takes in no parameters and returns a list like 105,98,91,...7
def while_it():
    n = 105
    a = []
    while n>=7:
        a.append(n)
        n-=7
    return a
def num_sum(N):
    s=0
    if N==0:
        return 0
    else:
        while N!=0:
            s+=N%10
            N = math.floor(N/10)#this acts as integer division
    return s
#greatest_integer returns the max and min out of three numbers
def greatest_integer(A,B,C):
    a = [None]*2
    if A>B:
        if A>C:
            a.append(A)
            if B>C:
                a.append(C)
                
            if B<C:
                a.append(B)
                
        if C>A:
            a.append(C)
            a.append(B)

    elif B>A:
        if B>C:
            a.append(B)
            if A>C:
                a.append(C)
            if C>A:
                a.append(A)
        if C>B:
            a.append(C)
            a.append(A)
    return a
#square_pair creates a combined list
def square_pair(L1,L2):
    l=[None]*(2*len(L1))
    if len(L1)==len(L2):
        for i in range(2*len(L1)):
            for j in range(2*len(L2),2):#logic fails if len(L1)!=len(L2)
                l[j] = L1[i]
            for k in range(1,len(L1)-1,2):
                l[k] = L2[i]
    else:
        l = -1
    return l
#main function
def main():
    N = int(input("Enter N for range roller:"))
    K = int(input("Enter K for range roller:"))
    print(range_roller(N,K))
    print(while_it)
    n = int(input("Enter N for num sum:"))
    print(num_sum(n))
    A = int(input("Enter integer A for greatest integer function:"))
    B = int(input("Enter integer B for greatest integer function:"))
    C = int(input("Enter integer C for greatest integer function:"))
    print(greatest_integer(A,B,C))
    length = int(input("Enter length of the lists for squared pair:"))
    L1 = L2 = [None]*length
    for i in range(length):
        L1[i] = int(input("Enter element ",i, " for the first list:"))
    for j in range(length):
        L2[j] = int(input("Enter element ",j," for second list which contains the squares:"))
    print(square_pair(L1,L2))
main()
        

        
            




    

    
        









