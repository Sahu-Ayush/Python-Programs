# Number Pattern

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4
1234
123
12
1


Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines


Sample Input :
5

Sample Output :
12345
1234
123
12
1
'''


# CODE #

n = int(input())
i = 1
p = n
while i <= n:
    j = 1
    while j <= p:
        print(j, end='')
        j += 1
    print()
    p -= 1
    i += 1
