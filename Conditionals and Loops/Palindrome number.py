# Palindrome number

'''
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121


Sample Input 1 :
121

Sample Output 1 :
true


Sample Input 2 :
1032

Sample Output 2 :
false
'''

# Code

def checkPalindrome(num):
    Reverse_no = 0
    n = num
    
    while n > 0:
        rem = n % 10
        Reverse_no += rem
        Reverse_no *= 10
        n //= 10

    return num == (Reverse_no // 10)
        
        
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
