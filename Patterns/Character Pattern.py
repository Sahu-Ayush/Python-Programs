# Character Pattern

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4
A
BC
CDE
DEFG


Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines


Constraints
0 <= N <= 13
S

ample Input 1:
5

Sample Output 1:
A
BC
CDE
DEFG
EFGHI


Sample Input 2:
6

Sample Output 2:
A
BC
CDE
DEFG
EFGHI
FGHIJK
'''

# CODE #

n = int(input())
i = 1

while i <= n:                                       # Outer while loop reprent numbers of rows
    j = 1
    starting_char = chr(ord("A") + i -1)            # starting_char represent starting scharacter for each new row
    while j <= i:                                   # Inner loop will execute till ith times to print i's no. of charater in the  row; in each iteration of outter loop; to
        charPrint = chr(ord(starting_char) + j -1)  # charPrint will character in the row and increment the charater for the row(each inner row)
        print(charPrint, end="")
        j += 1
    print()
    i += 1
