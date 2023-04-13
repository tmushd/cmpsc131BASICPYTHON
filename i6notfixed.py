class I6:
    s = 0
    def downhill(N):
        if N == 1:
            print(N)
            return
        print(N)
        downhill(N-1)

    def valley(N):
        cp = N # making a copy of the function so that the mutated value of N does not affect the loop
        if N == 1:
            print(N)
            print(N) #since 1 needs to be printed twice
            return
        print(N)
        valley(N-1)
        c=0
        c+=1
        print(N)
        if cp>N:
            for i in range(1,cp): # I used easy logic so that it makes sense to you. Delete this comment.
                print(i)

    def list_sum(list1,length):
        if length <= 0:
            s+=list1[length]
            print(s)
            return
        s+=list1[length-1]
        list_sum(list1,length-1)
    
    def digit_sum(N):
        if N%10==0:
            print(s)
            return
        s += (N%10)
        digit_sum(N//10)
    
#Figure out why list_sum and digit_sum are not working. Delete this comment.

def am():
    o = I6()
    a = int(input("Enter the integer N for downhill(): "))
    o.downhill(a)
    b = int(input("Enter the integer N for downhill(): "))
    o.valley(b)
    length = int(input("Enter the length of the list: "))
    list1=[]
    for i in range(length):
        list1.append(int(input("Enter element "+ str(i+1)+ " in the list ")))
    
    o.list_sum(list1,length)
    n = int(input("Enter n for digit_sum(): "))
    o.digit_sum(n)
        #I created main to test the functions
am()
