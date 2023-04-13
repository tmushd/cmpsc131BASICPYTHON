#fix the code without running it and explain why the bugs are bugs.
def calc_Area():
    m = int(input("Enter 1 for rectangle, 2 for square, 3 for circle, 4 for triangle"))
    if m==1:
        l = int(input("Enter the length of the rectangle"))
        b = int(input("Enter the width of the rectangle"))
        area = l*b
    elif m==2:
        s = int(input("Enter the side length of the square"))
        area = s*s
    elif m==3:
        r = int(input("Enter the radius of the circle"))
        area = 3.14*r*r
    elif m==4:
        b = int(input("Enter the base length for the triangle"))
        h = int(input("Enter the height of the triangle"))
        area = 0.5*b*h
        #bugs are fixed now.
    return area
def main():
    print(calc_Area())
main()
