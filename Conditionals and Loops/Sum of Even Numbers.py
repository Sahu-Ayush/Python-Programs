# Sum of Even Numbers

'''
Given a number N, print sum of all even numbers from 1 to N.


Input Format :
Integer N

Output Format :
Required Sum 


Sample Input 1 :
 6

Sample Output 1 :
12
'''

# Code

N = int(input())

count = 1
sum = 0

while count <= N:
    if count % 2 == 0:
        sum = sum + count
    count = count + 1
print(sum)
