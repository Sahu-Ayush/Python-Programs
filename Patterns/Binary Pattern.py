# Binary Pattern

'''
Print the following pattern for the given number of rows.


Pattern for N = 4
1111
000
11
0


Input format : N (Total no. of rows)

Output format : Pattern in N lines


Sample Input :
5

Sample Output :
11111
0000
111
00
1
'''

# Code

n = int(input())

i = 1
while i <= n:
    #
    j = 1
    while j <= n - i + 1:
        if i % 2 == 0:
            print("0", end='')
        else:
            print("1", end='')
        j += 1
    #
    print()
    i += 1
