# Reverse of a number

'''
Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

Note : If a number has trailing zeros,
then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.


Input format :
Integer N

Output format :
Corresponding reverse number


Constraints:
0 <= N < 10^8


Sample Input 1 :
1234

Sample Output 1 :
4321


Sample Input 2 :
1980

Sample Output 2 :
891
'''

# Code

'''
def reverse(n):
    Reverse_no = 0

    while n > 0:
        rem = n % 10
        Reverse_no += rem
        Reverse_no *= 10
        n //= 10

    return Reverse_no // 10

n=int(input())
result = reverse(n)
print(result)
'''

### OR ###

n = int(input())
temp = n
revNum = 0

while temp > 0:
	lastDigit = temp % 10
	temp = temp // 10
	revNum = revNum * 10 + lastDigit

print(revNum)
