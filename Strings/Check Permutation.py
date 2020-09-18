# Check Permutation

'''
Given two strings, S and T, check if they are permutations of each other. Return true or false.
Permutation means - length of both the strings should same and should contain same set of characters.
Order of characters doesn't matter.

Note : Input strings contain only lowercase english alphabets.


Input format :
Line 1 : String 1
Line 2 : String 2

Output format :
'true' or 'false'


Constraints :
0 <= |S| <= 10^7
0 <= |T| <= 10^7
where |S| represents the length of string, S.


Sample Input 1 :
abcde
baedc

Sample Output 1 :
true


Sample Input 2 :
abc
cbd

Sample Output 2 :
false
'''

# Code

def isPermutation(s1, s2):

    s1_length = len(s1)
    s2_length = len(s2)

    if s1_length == s2_length:
        pass
    else:
        return "false"

    li = []
    for ele in s1:
        li.append(ele)
    li.sort()
    s1 = [str(x) for x in li]
    li = []
    for ele in s2:
        li.append(ele)
    li.sort()
    s2 = [str(x) for x in li]

    if s1 == s2:
        return "true"
    else:
        return "false"

s1 = input()
s2 = input()
print(isPermutation(s1, s2))

### OR ###

'''
def isPermutation(s1, s2):
    freqCount = {}
    for char in s1:
        if char in freqCount:
            freqCount[char] += 1
        else:
            freqCount[char] = 1

    for char in s2:
        if char in freqCount:
            if freqCount[char] == 1:
                del freqCount[char]
            else:
                freqCount[char] -= 1
        else:
            return False

    if freqCount:
        return False
    return True

# Main
s1=input()
s2=input()
if isPermutation(s1, s2):
    print('true')
else:
    print('false')
'''
