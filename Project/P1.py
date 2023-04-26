import math
'''
Name- mayank futnani arupula
ID-mxa6067@psu.edu




'''

m = "/Users/mayankarupula/Downloads/box-1.txt"
def cleanse(m):
    L2=[]
    L3=[]
    s = ""
    contents=open(m,'r')
    #same as L4 solution.
    l=contents.readline()
    #l is a string form of contents
    while l!='':
        # use int() to convert to intergers
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
#end of first function'''

    
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


    min_num=len(b[0])
    min_color=b[0][0]
    for i in range(len(b)):
        if (len(b[i])<min_num):
            min_num=len(b[i])
            min_color=b[i][0]
    return [max_color,min_color]
#end of second function

def color_deviation(cleanse(m)):
    li = cleanse(m)
    s1 = 0.0#sum to calculate mean
    s2 = 0.0#sum to calculate (xi - mean)^2
    avg = 0.0#stores mean
    a = []#client list
    S = 0.0#S = population standard deviation
    for i in range(len(li)):
        for j in range(1, len(li[i]))
            s1+=li[i][j]
        avg = s1/len(li[i])
        for k in range(1, len(li[i]))
            s2 += (li[i][j]-avg)**2
        S = math.sqrt(s2/len(li[i]))
        a+=S
    return a
#end of third function

def rainbow_check(cleanse(m)):
    li = cleanse(m)
    r = -6
    a=[]
    for i in range(len(li))
        if li[i] == 'Violet':
            r+=1
            a+=i
        if li[i] == 'Indigo':
            r+=1
            a+=i
        if li[i] == 'Blue':
            r+=1
            a+=i
        if li[i] == 'Green':
            r+=1
            a+=i
        if li[i] == 'Yellow':
            r+=1
            a+=i
        if li[i] == 'Orange':
            r+=1
            a+=i
        if li[i] == 'Red':
            r+=1
            a+=i
    if r==1:
        return 1,a
    else:
        return a
#end of fourth function        

def happy_kids(cleanse(m)):
    x = input("Enter the value of x: ")
    li = cleanse(m)
    c = 0
    for i in range(len(li)):
        if x == li[i]:
            c+=1
    return c
#end of fifth function
    
    
def main():
    print(cleanse(m))
    a = cleanse(m)
    print(color_count(a))
    print(color_deviation(a))
    print(rainbow_check(a))
    print(happy_kids(a))
main()
