# Print Number Pyramid

'''
Print the following pattern for a given n.

For eg. N = 6
123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456


Sample Input 1 :
4

Sample Output 1 :
1234
 234
  34
   4
  34
 234
1234
'''

# Code

n = int(input())

for i in range(1, n + 1):
    for space in range(1, i):
        # print("@", end='')
        print(" ", end='')
    for j in range(i, n + 1):
        print(j, end='')
    print()

for i in range(1, n):
    for space in range(1, n - i):
        # print("@", end='')
        print(" ", end='')
    for j in range(n - i, n + 1):
        print(j, end='')
    print()
