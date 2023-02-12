def gradeit(double x):
    if x>=80.0 and x<=100.0:
        return A
    if x>=50.0:
        return B
    if x<50.0 and x>0:
        return C
    if x>100 or x<0:
        return I
def main():
    print(gradeit(50))
main()
