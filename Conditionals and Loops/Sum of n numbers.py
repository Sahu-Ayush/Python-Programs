# Sum of n numbers

'''
Given an integer n, find and print the sum of numbers from 1 to n.
Note : Use while loop only.


Input Format :
Integer n

Output Format :
Sum


Constraints :
1 <= n <= 100


Sample Input :
10

Sample Output :
55
'''

# Code

n = int(input())

count = 1
s = 0
while count <= n:
    s = s + count
    count = count + 1
print(s)
