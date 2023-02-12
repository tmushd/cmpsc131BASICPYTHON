import math
#Problem1
def avg_num(a,b):
    avg = (a+b)/2
    return avg
def print_str(s):
    print(s)
def my_num():
    return 9;
def hello_msg():
    print("hello world")
#
#Problem2
def exp_growth():
    A = int(input("Enter the initial population"))
    k = float(input("Enter the growth rate"))
    t = int(input("Enter the time in years"))
    e = 2.7
    P = A*e**(k*t)
    return P
#
#Problem3
def point_distance():
    x1 = float(input("Enter the x coordiante of the first point"))
    y1 = float(input("Enter the y coordinate of the first point"))
    x2 = float(input("Enter the x coordinate of the second"))
    y2 = float(input("Enter the y coordinate of the second point"))
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d
#
#Problem4
def slope():
    x1 = float(input("Enter the x coordiante of the first point"))
    y1 = float(input("Enter the y coordinate of the first point"))
    x2 = float(input("Enter the x coordinate of the second"))
    y2 = float(input("Enter the y coordinate of the second point"))
    m = (y2-y1)/(x2-x1)
    return m
#
#main function
def main():
    av = avg_num(5,3)
    print("The average is",av)
    print_str("Hi, my name is vayu")
    fav = my_num()
    print("My favorite number is ",fav)
    hello_msg()
    #invoking problem 2 function
    est = exp_growth()
    print("The estinated population of the country is",est)
    #invoking problem 3 function
    d = point_distance()
    print("The distance between the two points is: ",d)
    m = slope()
    print("The slope of the line segment between the two given points is ",m)
main()


    





