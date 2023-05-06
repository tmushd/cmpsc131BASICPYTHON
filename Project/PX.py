import math as m
'''
Name- mayank futnani arupula
ID-mxa6067@psu.edu




'''

c = "/Users/mayankarupula/Downloads/box-1.txt"
def cleanse(c):
    L2=[]
    L3=[]
    s = ""
    contents=open(c,'r')
    #same as L4 solution.
    l=contents.readline()
    #l is a string form of contents
    while l!='':
        # use int() to convert to integers
        l = l.strip().split()
        flag = 0
        for i in range(len(L2)):
            if L2[i][0] == l[0]:
                flag = 1
        if flag == 0:
            L2+=[l]
        l=contents.readline()

    for i in range(len(L2)):
        
        for j in range(1, len(L2[i])):
            L2[i][j] = int(L2[i][j])
        
    return L2
#end of first function

    
def color_count(k):
    r = []
    b = k
    n = len(b)
    max_num=len(b[0])
    max_color=b[0][0]
    for i in range(len(b)):
        if (len(b[i])>max_num):
            max_num=len(b[i])
            max_color=b[i][0]
            #max color stored
    min_num=len(b[0])
    min_color=b[0][0]
    for i in range(len(b)):
        if (len(b[i])<min_num):
            min_num=len(b[i])
            min_color=b[i][0]
            #min color stored
    return [max_color,min_color]
# returned as list
#end of second function

def color_deviation(cleanse(c)):
    l1 = cleanse(c)
    s1 = 0.0
    s2 = 0.0
    mean = 0.0
    a = []
    S = 0.0
    for i in range(len(l1)):
        for j in range(1, len(l1[i]))
            s1+=l1[i][j]
        mean = s1/len(l1[i])
        for k in range(1, len(l1[i]))
            s2 += (m.pow((l1[i][j]-mean),2))
        S = m.sqrt(s2/len(l1[i]))
        a+=S
    return a
#end of third function

def rainbow_check(cleanse(c)):
    l1 = cleanse(c)
    r = -6
    a=[]
    for i in range(len(l1))#VIBGYOR
        if l1[i] == 'Violet':
            r+=1
            a+=i
        if l1[i] == 'Indigo':
            r+=1
            a+=i
        if l1[i] == 'Blue':
            r+=1
            a+=i
        if l1[i] == 'Green':
            r+=1
            a+=i
        if l1[i] == 'Yellow':
            r+=1
            a+=i
        if l1[i] == 'Orange':
            r+=1
            a+=i
        if l1[i] == 'Red':
            r+=1
            a+=i
    if r==1:
        return 1,a
    else:
        return a
#end of fourth function        

def happy_kids(cleanse(c)):
    x = input("Enter the value of x: ")
    l1 = cleanse(c)
    a = 0
    for i in range(len(l1)):
        if x == l1[i]:
            a+=1
    return a
#end of fifth function
    
    
def main():
    #main for checks
    print(cleanse(m))
    a = cleanse(m)
    print(color_count(a))
    print(color_deviation(a))
    print(rainbow_check(a))
    print(happy_kids(a))
main()
