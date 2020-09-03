# Interesting Alphabets

'''
Print the following pattern for the given number of rows.

Pattern for N = 5
E
DE
CDE
BCDE
ABCDE


Input format :
N (Total no. of rows)

Output format :
Pattern in N lines


Constraints
0 <= N <= 26


Sample Input 1:
8

Sample Output 1:
H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH


Sample Input 2:
7

Sample Output 2:
G
FG
EFG
DEFG
CDEFG
BCDEFG
ABCDEFG
'''

# CODE #

n = int(input())
i = n

while i >= 1:           # Outer loop represent rows, which execute till ith or nth times in decriment order
    j = n               # j initialized by n in row (in each outer iteration)
    p = 0               # p initialized by 0 in row (in each outer iteration)
    ending_char = chr(ord("A") + i - 1)     # Inner loop will execute till ith (and j will decriment) times to print i's no. of charater in the  row; in each iteration of outter loop; to
    while j >= i:                           # charPrint will character in the row and increment the charater for the row(each inner row
        char_print = chr(ord(ending_char) + p)
        print(char_print, end="")
        j -= 1
        p += 1
    print()
    i -= 1
