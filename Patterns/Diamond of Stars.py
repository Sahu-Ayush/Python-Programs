# Diamond of Stars

'''
Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5
  *
 ***
*****
 ***
  *


Input format :
N (Total no. of rows and can only be odd)

Output format :
Pattern in N lines


Constraints :
1 <= N <= 49


Sample Input 1:
5

Sample Output 1:
  *
 ***
*****
 ***
  *


Sample Input 2:
3

Sample Output 2:
 *
***
 *
'''

# Code

n = int(input())

first_half_n = n // 2 + 1
second_half_n = n // 2
# Printing first half part of the diamond
#i = 1
for i in range(1, first_half_n + 1):
#while i <= first_half_n:
    # Decreasing space
#    space = 1
    for space in range(1, (first_half_n + 1) - i):
#    while space <= first_half_n - i:
#        print("@", end='')
        print(" ",end='')
#        space += 1
    # Increasing Mirror image (first part of upper diamond))
#    j = 1
    for j in range(1, i + 1):
#    while j <= i:
        print("*", end='')
#        j += 1
    # Second part of upper diamond
#    p = i - 1
    for p in range(i - 1, 0, -1):
#    while p >= 1:
        print("*", end='')
#        p -= 1
    #
    print()
    i += 1

# Printing second half part of the diamond
#i = 1
for i in range(1, second_half_n + 1):
#while i <= second_half_n:
    # Increasing space
#    space = 1
    for space in range(1, i + 1):
#    while space <= i:
#        print("@", end='')
        print(" ",end='')
#        space += 1
    # Decreasing Mirror of the second half of the diamond
#    j = 1
    for j in range(1, (second_half_n - i + 1) + 1):
#    while j <= second_half_n - i + 1:
        print("*", end='')
#        j += 1
    # Decreasing Inverted triangle second half of the diamond
#    p = 1
    for p in range(1, (second_half_n + 1) - i):
#    while p <= second_half_n - i:
        print("*", end='')
#        p += 1
    #
    print()
    i += 1
