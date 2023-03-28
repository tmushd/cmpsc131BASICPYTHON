import math as m

def calc_Area():
    m = input("Enter 1 for rectangle, 2 for square, 3 for circle, 4 for triangle")
    if m==1:
        l = input("Enter the length of the rectangle")
        b = input("Enter the width of the rectangle")
        area = l*b
    elif m==2:
        s = input("Enter the side length of the square")
        area = s*s
    elif m==3:
        r = input("Enter the radius of the circle")
        area = m.pi*r*r
    elif m==4:
        b = input("Enter the base lenght for the triangle")
        h = input("Enter the height of the triangle")
        area = 0.5*b*h
    return area
def main():
    area = 0
    print(calc_Area())
main()
