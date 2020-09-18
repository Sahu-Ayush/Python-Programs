# Fibonacci Member Function

'''
Given a number N, figure out if it is a member of fibonacci series or not.
Return true if the number is member of fibonacci series else false.


Fibonacci Series is defined by the recurrence
    F(n) = F(n-1) + F(n-2)
where F(0) = 0 and F(1) = 1


Input Format :
Integer N

Output Format :
true or false


Constraints :
0 <= n <= 10^4


Sample Input 1 :
5

Sample Output 1 :
true


Sample Input 2 :
14

Sample Output 2 :
false
'''

# Code

'''
import math

def isPerfectSquare(n):
    s = int(math.sqrt(n))
    return s * s == n

def checkMember(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
'''

### OR  ###

def checkMember(n):
    if (n==0 or n==1 or n==2):
        return True
    a=0
    b=1
    while b<n:
        c=a+b
        a=b
        b=c
    if b==n:
        return True

    return False

# Main
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
