# Number Pattern 3

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4
1
11
121
1221


Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines


Sample Input :
5

Sample Output :
1
11
121
1221
12221
'''


# CODE #

n = int(input())
i = 1

while i <= n:
    j = 1
    p = i
    while j <= i:
        if i == p and j == 1:
            print(1, end='')
        elif j == i:
            print(1, end='')
        else:
            print(2, end='')
        j += 1
    print()
    i += 1
