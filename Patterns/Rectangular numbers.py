# Rectangular numbers

'''
Print the following pattern for the given number of rows.


Pattern for N = 4
4444444
4333334
4322234
4321234
4322234
4333334  
4444444


Input format : N (Total no. of rows)

Output format : Pattern in N lines


Sample Input :
3

Sample Output :
33333
32223
32123
32223
33333
'''

# Code

n = int(input())

for i in range(n, 0, -1):
    for j in range(n, i - 1, -1):
        print(j, end='')
    for j in range(1, (i * 2) - 1):
        print(i, end='')
    for j in range(i + 1, n + 1):
        print(j, end='')
    print()

for i in range(2, n + 1):
    for j in range(n, i - 1, -1):
        print(j, end='')
    for j in range(1, (i * 2) - 1):
        print(i, end='')
    for j in range(i + 1, n + 1):
        print(j, end='')
    print()
