# imported library,
# re            for using regex
# prettytable   for using formated table
import re
import prettytable

# array for inputted numbers
NUMBERS = []

# procedure sort, for sorting the numbers array (ASC) using selection sort.
def sort():
    # loop trough the array NUMBERS
    for i in range(0, len(NUMBERS)):
        minIndex = i    # declare initial index

        # loop trough the array NUMBERS, start form index i+1
        for j in range(i+1, len(NUMBERS)):
            if(NUMBERS[minIndex]>NUMBERS[j]):
                # if number with minIndex number is larger than number with j index, 
                # than replace minIndex value with j
                minIndex = j

        # process for swap the array value with the smaller number
        temp = NUMBERS[i]
        NUMBERS[i] = NUMBERS[minIndex]
        NUMBERS[minIndex] = temp

# fuction average, returning the average number from array NUMBERS
def average():
    total = 0   # declare variable for the sum of numbers

    # loop trough array NUMBER
    for number in NUMBERS:
        total += number         # sum the number

    return total/len(NUMBERS)   # return average from total divided by lenght of the array NUMBERS

# fuction median, returning the mid number from array NUMBERS
def median():
    if(len(NUMBERS) == 1):
        # if the array only contain 1 number
        # return the number 
        return NUMBERS[0]
    elif(len(NUMBERS)%2 != 0):
        # if the array number lenght is odd
        # return the number on index -1n/2
        return NUMBERS[int((len(NUMBERS)-1)/2)]
    else:
        # if the array number lenght is even,
        # return the number on index (n/2)-1 + (n/2) devided by 2
        return (NUMBERS[int((len(NUMBERS)/2)-1)] + NUMBERS[int((len(NUMBERS)/2))])/2

# fuction multiply, returning the multiplication result from array NUMBERS
def multiply():
    total = 1   # declare variable for the muliplication of numbers
    
    # loop trough array NUMBER
    for number in NUMBERS:
        total *= number # multiply each number

    return total        # return the result

# procedure print_table, for print array NUMBERS data on formatted table.
def print_table():
    # initialize the table with the header value
    table = prettytable.PrettyTable(['#', 'Number'])

    # loop trough array NUMBER
    for i in range(0, len(NUMBERS)):
        # add each number to table row
        table.add_row([i+1, NUMBERS[i]])
    
    print(table) # print the table


ex = False  # variable for looping the program
reg_dec = re.compile(r"^\d+(?:\.\d*)?$")    # regex rule

print("Welcome to the Numbers Program!")

# loop when ex value is False
while(ex == False): 
    if(len(NUMBERS)):
        # if there is numbers on array NUMBERS

        # process for print the table
        print("Curent Numbers : ")
        sort()          # sort the array NUMBER
        print_table()   # print the table
        print("Average    = " + str(round(average(),2)))    # print average number
        print("Median     = " + str(round(median(),2)))     # print median number
        print("MLP Result = " + str(round(multiply(),2)))   # print multiplication result
        

    print("Input numbers to perform the program or type 'exit' to close the program.")
    
    # get input from user
    data = input("> ")      
    if(reg_dec.match(data)):
        # if inputted data match regex rules
        if(data.isnumeric()):
            # if number is integer
            # add to array as integer number
            NUMBERS.append(int(data))
        else:
            # if number is float
            # add to array as float number
            NUMBERS.append(float(data))  
    else:
        # if inputted data doesn't match regex rules
        if(data.lower() == 'exit'):
            # if the value is exit
            # set variable ex to True, so the program stop looping
            ex = True
        else:
            # if the inputted data is other than number and exit
            # print this message
            print("! Unrecognize input")
    