# numbers-program

## About
this is a python program for processing numbers where it will receive a number input from the user and return the sorted numbers with the average, median, and multiplication result of the numbers.

## Getting Started
To run the program, make sure you have installed python on your device. Also, install this libraries:
1. re (library for regex)
2. prettytable (library for formatting table)

After all above, run the program and it will ask you for the input and it will process your input. more explanation for the input and output, read below:

### Input 
1. Integer number (e.g. 25)
2. Float number, seperated by '.' (e.g. 2.4)
3. 'exit' for close the program

Other input than above limitation will returning `! Unrecognize input`

### Output
1. List of the numbers
2. Average
3. Median
4. MLP Result

Example output:
```sh
Curent Numbers : 
+---+--------+
| # | Number |
+---+--------+
| 1 |   1    |
| 2 |  1.2   |
| 3 |  2.6   |
| 4 |  3.1   |
| 5 |   12   |
| 6 |   12   |
| 7 |   14   |
+---+--------+
Average    = 6.56
Median     = 3.1
MLP Result = 19498.75
```