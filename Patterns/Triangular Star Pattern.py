# Triangular Star Pattern

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4
*
**
***
****

Note : There are no spaces between the stars (*).

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Constraints
0 <= N <= 50


Sample Input 1:
5

Sample Output 1:
*
**
***
****
*****


Sample Input 2:
6

Sample Output 2:
*
**
***
****
*****
******
'''

### CODE ###

n = int(input())
i = 1

while i <= n:               # Outer while loop reprent numbers of rows
    j = 1
    while j <= i:           # i numbers of stras print in the row
        print("*", end="")
        j += 1
    print()
    i += 1
