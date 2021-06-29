import re
import prettytable

NUMBERS = []

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
print("Input numbers to perform the program or type 'exit' to close the program.")

while(ex == False):
    if(len(NUMBERS)):
        print("Curent Numbers : ")
        NUMBERS.sort()
        print_table()
        print("Average    = " + str(average()))
        print("Median     = " + str(median()))
        print("MLP Result = " + str(multiply()))
        

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