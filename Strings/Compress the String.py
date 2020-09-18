# Compress the String

'''
Write a program to do basic string compression.
For a character which is consecutively repeated more than once,
replace consecutive duplicate occurrences with the count of repetitions.

Exmple:
If a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".

The string is compressed only when the repeated character count is more than 1.

Note :
Consecutive count of every character in the input string is less than equal to 9.


Input Format :
The first and the only line of input contains a string(no spaces in between).

Output Format :
The only line of output print the compressed string.

Note:
Return the compressed string and hence, no need to print.


Constraints :
0 <= |S| <= 10^7
Where |S| represents the length of string, S.
Time Limit: 1sec


Sample Input 1 :
aaabbccdsa

Sample Output 1 :
a3b2c2dsa


Sample Input 2 :
aaabbcddeeeee

Sample Output 2 :
a3b2cd2e5
'''

# Code

def compressString(s):
    reserved = ""
    count = 1
    reserved += s[0]

    for i in range(len(s) - 1):
        if(s[i] == s[i + 1]):
            count += 1
        else:
            if(count > 1):
                reserved += str(count)
            reserved += s[i + 1]
            count = 1
    if(count > 1):
        reserved += str(count)
    return reserved

s = input()
print(compressString(s))

### OR ###

'''
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def getCompressedString(s):
    ans = s[0]
    i, length = 1, len(s)
    while i<length:
        if ans[-1]==s[i]:
            count=2
            i += 1
            while i<length and ans[-1]==s[i]:
                count += 1
                i += 1
            ans += str(count)
        else:
            ans += s[i]
            i += 1
    return ans


#taking inpit using fast I/O
def takeInput() :
	
    str1 = input().strip()
    return str1


#main
str1 = takeInput()
print(getCompressedString(str1))
'''
