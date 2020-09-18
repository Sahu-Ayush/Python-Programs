# Nth Fibonacci number

'''
Nth term of fibonacci series F(n) is calculated using following formula -
    F(n) = F(n-1) + F(n-2), 
    Where, F(1) = F(2) = 1
Provided N you have to find out the Nth Fibonacci Number.


Input Format :
Integer n

Output Format :
Nth Fibonacci term i.e. F(n)


Constraints:
1 <= n <= 25


Sample Input 1:
4
Sample Output 1:
3 


Sample Input 2:
6
Sample Output 2:
8
'''

# Code

'''
n = int(input())

a = 1
b = 1
temp = 0
it = 3

if n > it:
    while it <= n:
        temp = a + b
        a = b
        b =temp
        it += 1
    print(temp)
elif n == 1 or n ==2:
    print(a)
elif n == 0:
    print(temp)
'''
## OR ###
    
n = int(input())

a = 0
b = 1
c = 0

for i in range(n):
    c = a+b
    a = b
    b = c
    
print(a)
