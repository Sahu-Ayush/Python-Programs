# Triangle of Numbers

'''
Print the following pattern for the given number of rows.

Pattern for N = 4
   1
  232
 34543
4567654
Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines


Constraints :
0 <= N <= 50


Sample Input 1:
5

Sample Output 1:
    1
   232
  34543
 4567654
567898765


Sample Input 2:
4

Sample Output 2:
   1
  232
 34543
4567654
'''

# Code

n = int(input())

i = 1
while i <= n:
    # Printing space through n - i
    space = 1
    while space <= n - i:
        print(" ", end='')
        space += 1

    # Increasing Sequence
    j = 1
    print_num = i
    while j <= i:
        print(print_num, end='')
        print_num += 1
        j += 1

    # Decreasing Sequence
    last_value_j = print_num - 2
    p = i - 1
    while p >= 1:
        print(last_value_j, end='')
        p -= 1
        last_value_j -= 1
    print()
    i += 1
