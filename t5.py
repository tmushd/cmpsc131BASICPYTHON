def total_sales(sales):
    total = 0
    new_list = [0]*(len(sales)+1)
    i = 0
    for i in range(len(sales)):
        total += sales[i]
        new_list[i] = sales[i]
    new_list[i+1] = total
    return new_list

def main():
    # Test the total_sales() function
    a = [14, 15, 16, 17, 18, 19, 20]
    print("New sales:", total_sales(a))
main()
