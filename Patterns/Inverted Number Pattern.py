# Inverted Number Pattern

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4
4444
333
22
1


Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines


Constraints :
0 <= N <= 50


Sample Input 1:
5

Sample Output 1:
55555 
4444
333
22
1


Sample Input 2:
6

Sample Output 2:
666666
55555 
4444
333
22
1
'''

# Code

n = int(input())

# Printing Inverted Number
i = 1
while i <= n:
    j = 1
    while j <= n - i + 1:    # n - i + 1 has inverted the numver
        print(n - i + 1, end='')
        j += 1
    print()
    i += 1
