# Number Pattern 2

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4
1
11
202
3003


Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines


Sample Input :
5

Sample Output :
1
11
202
3003
40004
'''

# CODE #

'''
n = int(input())
i = 1

if n > 0:
    while i <= n:
        j = 1
        p = i
        while j <= i:

            if i == p and j == 1:
                if i == 1 and j ==1:
                    print(1, end='')
                else:
                    print(i - 1, end='')
            elif j == i:
                print(i - 1, end='')
            else:
                print(0, end='')
            j += 1
        print()
        i += 1
else:
    print(1)
'''

### OR ###


n = int(input())
print(1)
i = 1
while i < n:
    j = 0
    while j < i+1:
        if j==0 or j==i:
            print(i,end='')
        else:
            print(0,end="")
        j = j + 1
    print()
    i = i + 1
