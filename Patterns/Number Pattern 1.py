# Number Pattern 1

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4
1
11
111
1111


Input format :
Integer N (Total no. of rows)


Output format :
Pattern in N lines


Sample Input :
5

Sample Output :
1
11
111
1111
11111
'''

# CODE #

n = int(input())
i = 1

while i <= n:
    j = 1
    p = 0
    while j <= i:
        print(j - p , end="")
        j += 1
        p += 1
    print()
    i += 1
