# Star Pattern

'''
Print the following pattern

Pattern for N = 4
   *
  ***
 *****
*******


Input Format :
N (Total no. of rows)

Output Format :
Pattern in N lines


Constraints :
0 <= N <= 50


Sample Input 1 :
3

Sample Output 1 :
  *
 *** 
*****


Sample Input 2 :
4

Sample Output 2 :
   *
  *** 
 *****
*******
'''

# Code

n = int(input())

i = 1
add_no_of_start = 0
while i <= n:
    # Printing space through n - i
    space = 1
    while space <= n - i:
        print(" ", end='')
        space += 1

    # Printing the stars
    j = 1
    while j <= i + add_no_of_start:
        print("*", end='')
        j += 1
    print()
    i += 1
    add_no_of_start += 1
