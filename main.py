import re
import prettytable

NUMBERS = []

def sort():
    for i in range(0, len(NUMBERS)):
        minIndex = i

        for j in range(i+1, len(NUMBERS)):
            if(NUMBERS[minIndex]>NUMBERS[j]):
                minIndex = j

        temp = NUMBERS[i]
        NUMBERS[i] = NUMBERS[minIndex]
        NUMBERS[minIndex] = temp
def average():
    total = 0
    for number in NUMBERS:
        total += number
    return total/len(NUMBERS)
def median():
    if(len(NUMBERS) == 1):
        return NUMBERS[0]
    elif(len(NUMBERS)%2 != 0):
        return NUMBERS[int((len(NUMBERS)-1)/2)]
    else:
        return (NUMBERS[int((len(NUMBERS)/2)-1)] + NUMBERS[int((len(NUMBERS)/2))])/2
def multiply():
    total = 1
    for number in NUMBERS:
        total *= number
    return total
def print_table():
    table = prettytable.PrettyTable(['#', 'Number'])
    for i in range(0, len(NUMBERS)):
        table.add_row([i+1, NUMBERS[i]])
    
    print(table)


ex = False
reg_dec = re.compile(r"^\d+(?:\.\d*)?$")

print("Welcome to the Numbers Program!")

while(ex == False):
    if(len(NUMBERS)):
        print("Curent Numbers : ")
        sort()
        print_table()
        print("Average    = " + str(round(average(),2)))
        print("Median     = " + str(round(median(),2)))
        print("MLP Result = " + str(round(multiply(),2)))
        

    print("Input numbers to perform the program or type 'exit' to close the program.")
    data = input("> ")
    if(reg_dec.match(data)):
        if(data.isnumeric()):
            NUMBERS.append(int(data))
        else:
            NUMBERS.append(float(data))  
    else:
        if(data.lower() == 'exit'):
            ex = True
        else:
            print("! Unrecognize input")
    