# Mirror Number Pattern
'''
Print the following pattern for the given N number of rows.

Pattern for N = 4
   1 
  12
 123
1234


Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines


Constraints
0 <= N <= 50


Sample Input 1:
3

Sample Output 1:
  1 
 12
123


Sample Input 2:
4

Sample Output 2:
   1 
  12
 123
1234
'''

# Code

n = int(input())

i = 1
while i <= n:
    # Printing Spacing
    space = 1
    while space <= n - i:
        print(" ", end='')
        space += 1
    # Printing Mirror Number
    mirror_num = 1
    while mirror_num <= i:
        print(mirror_num, end='')
        mirror_num += 1
        
    print()
    i += 1
