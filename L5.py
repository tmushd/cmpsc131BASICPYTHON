#This is the entire program for your L5.py
def avg_row(l1):
  numrows = len(l1)
  numcolumns = len(l1[0])
  s = 0
  for i in range(numrows):
    for j in range(numcolumns):
      s+=l1[i][j]
    l1[i].append(s/numcolumns)
return l1
#end of function 1 test in your debugger and GPT
#IMPORTANT: Remove comment after tests.

def add_col(l2):
  numrows = len(l2)
  numcolumns = len(l2[0])
  l_2,s = [],0
  for i in range(numcolumns):
    for j in range(numrows):
      s+=l2[i][j]
    l_2.append(s)
return l_2
#end of function 2 test in your debugger and GPT
#IMPORTANT: Remove comment after tests.

def read_datafile(pathname):
    '''
    Accepts a pathname as an argument and returns a 2D list of floating point numbers.
    Assumes the first row contains header information and all subsequent rows contain whitespace separated floating point numbers.
    '''
    #DELETE THE ABOVE IN '''... '''
    with open(pathname, 'r') as file:
        # Read the header row and ignore it
        file.readline()
        # Initialize an empty list to store the data
        data = []
        # Loop over each subsequent line and append a list of floating point numbers to the data list
        for line in file:
            data.append([float(num) for num in line.split()])
        # Return the data as a 2D list
        return data
#End of function 3, I am a little unsure about this since I couldn't test this myself.
#I will prettify in main()

def avg_col(l4):
  numrows = len(l4)
  numcolumns = len(l4[0])
  l_4,s = [],0
  for i in range(numcolumns):
    for j in range(numrows):
      s+=l3[i][j]
    l_4.append(s)
l4.append(l_4)
return l4
#End of function 4.

def main():
  m1 = int(input('For function avg_rows() number of rows, m = '))
  n1 = int(input('For function avg_rows() number of columns, n = '))
  l1 = [[0 for j in range(n)] for i in range(m)]
  #I feel this is a nice way of taking input, you can modify if you like
  out1 = avg_rows(l1)
  print("The solution of avg_rows is: ", out1)
  
  #taking input of function 2
  m2 = int(input('For function add_col() number of rows, m = '))
  n2 = int(input('For function add_col() number of columns, n = '))
  l2 = [[0 for j in range(n)] for i in range(m)]
  #I feel this is a nice way of taking input, you can modify if you like
  out2 = add_col(l2)
  print("The solution of add_col is: ", out2)
  
  #taking input of function 3
  #BE CAREFUL with this
  localPathname = ""#paste your local pathname here
  print("The solution of read_datafile is: ",read_datafile(localPathname))
  
  #taking input of function 4
  m = int(input('For function avg_col() number of rows, m = '))
  n = int(input('For function avg_col() number of columns, n = '))
  l4 = [[0 for j in range(n)] for i in range(m)]
  #I feel this is a nice way of taking input, you can modify if you like
  out4 = avg_col(l4)
  print("The solution of avg_col is: ", out4)
main()
  
  
  
  
      
  
    
  
