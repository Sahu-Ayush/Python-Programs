#  Reverse Number Pattern

'''
Print the following pattern for the given N number of rows.


Pattern for N = 4

1
21
321
4321


Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines


Constraints
0 <= N <= 50


Sample Input 1:
5

Sample Output 1:
1
21
321
4321
54321


Sample Input 2:
6

Sample Output 2:
1
21
321
4321
54321
654321
'''

# CODE #

n = int(input())
i = 1

while i <= n:               # Outer while loop reprent numbers of rows
    j = 1                   
    p = i                   # starting point to print the nos. in revrese order(example if p=2, then 2,1)
    while j <= i:           # Inner loop will execute till ith times to print i's no. in the  row; in each iteration of outter loop; to
        print(p, end="")    # print the pth values in dercementing order
        j += 1
        p -= 1              # Decrimenting pth value
    print()
    i += 1
