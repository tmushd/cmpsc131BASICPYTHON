'''
Name- mayank futnani arupula
ID-mxa6067@psu.edu




'''

#m = "/Users/mayankarupula/Downloads/box-1.txt"
m = "/home/box-1.txt"
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
    avg = []
    S = 0.0#S = population standard deviation
    for i in range(1,len(li[i])):
        s+=li[i]
    avg = s/
        
    
    return S
    
def main():
    print(cleanse(m))
    print(color_count(a))

#main for testing
main()
