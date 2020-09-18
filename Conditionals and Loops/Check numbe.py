# Check numbe

'''
Given an integer n, find if n is positive, negative or 0.
If n is positive, print "Positive"
If n is negative, print "Negative"
And if n is equal to 0, print "Zero".

Input Format :
Integer n

Output Format :
"Positive" or "Negative" or "Zero" (without double quotes)


Constraints :
1 <= n <= 100


Sample Input 1 :
10

Sample Output 1 :
Positive


Sample Input 2 :
-10

Sample Output 2 :
Negative
'''

# Code

n = int(input())

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
