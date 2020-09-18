# Remove Consecutive Duplicates

'''
Given a string, S, remove all the consecutive duplicates that are present in the given string.
That means, if 'aaa' is present in the string then it should become 'a' in the output string.


Input format :
String S

Output format :
Modified string


Constraints :
0 <= |S| <= 10^7
where |S| represents the length of string, S.


Sample Input 1:
aabccbaa

Sample Output 1:
abcba


Sample Input 2:
xxyyzxx

Sample Output 2:
xyzx
'''

# Code

def removeConsecutiveDuplicates(s):
    n = len(s)
    if n < 2:
        return
    j = 0
    for i in range(n):
        if s[j] != s[i]:
            j += 1
            s[j] = s[i]
    j += 1
    s = s[:j]
    return s


s = input()
s1 = list(s.rstrip())
s = removeConsecutiveDuplicates(s1)
print(*s, sep = '')


### OR ###

'''
def removeConsecutiveDuplicates(s): 
    
    index=1
    while index<len(s):
        if s[index] == s[index-1]:
            nextIndex = index + 1
            length = len(s)
            while nextIndex<length and s[nextIndex] == s[index]:
                nextIndex += 1
            s = s[:index] + s[nextIndex:]
        else:
            index += 1
    return s

s = input()
print(removeConsecutiveDuplicates(s))
'''
