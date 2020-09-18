# Sum of Two Arrays

'''
Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively. Both the arrays/lists contain numbers from 0 to 9(i.e. single digit integer is present at every index). The idea here is to represent each array/list as an integer in itself of digits N and M.
You need to find the sum of both the input arrays/list treating them as two integers and put the result in another array/list i.e. output array/list will also contain only single digit at every index.

Note:
The sizes N and M can be different. 

Output array/list(of all 0s) has been provided as a function argument. Its size will always be one more than the size of the bigger array/list. Place 0 at the 0th index if there is no carry. 

No need to print the elements of the output array/list.


Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements of the first array/list.

Third line contains an integer 'M' representing the size of the second array/list.

Fourth line contains 'M' single space separated integers representing the elements of the second array/list.

Output Format :
For each test case, print the required sum of the arrays/list in a row, separated by a single space.

Output for every test case will be printed in a separate line.


Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
0 <= M <= 10^5
Time Limit: 1 sec 


Sample Input 1:
1
3
6 2 4
3
7 5 6

Sample Output 1:
1 3 8 0


Sample Input 2:
2
3
8 5 2
2
1 3
4
9 7 6 1
3
4 5 9

Sample Output 2:
0 8 6 5
1 0 2 2 0
'''


# Code

from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    i = n - 1
    j = m - 1
    carry = 0
    k = max(n, m)
    while i >= 0 and j >= 0 :
        SUM = arr1[i] + arr2[j] + carry
        output[k] = SUM % 10
        carry = SUM // 10
        i -= 1
        j -= 1
        k -= 1
    while i >= 0 :
        SUM = arr1[i] + carry
        output[k] = SUM % 10
        carry = SUM // 10
        i -= 1
        k -= 1
    while j >= 0 :
        SUM = arr2[i] + carry
        output[k] = SUM % 10
        carry = SUM // 10
        j -= 1
        k -= 1
    output[0] = carry

#Your code goes #Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n

#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()

#Main
t = int(stdin.readline().rstrip())
while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1

#### OR ####

'''
def sumOfTwoArray(arr1, arr2, n, m):
    ans = [0] * (max(n,m) + 1)
	# print("n ", n)

    i = n - 1
    j = m - 1
    a = max(m,n)
    carry = 0

    while i >= 0 and j >= 0:
		# print("i ", i)
        sumv = arr1[i] + arr2[j] + carry
		# print(arr1[i], arr2[j], carry)
		# print("sumv ", sumv)
        carry = 0
        if sumv > 9:
            ans[a] = sumv % 10
            carry = sumv // 10
        else:
            ans[a] = sumv
		# print("a ", ans)

        i -= 1
        j -= 1
        a -= 1
	# print("i ", i)

    while i >= 0:
        sumv = arr1[i] + carry
        carry = 0
        if sumv > 9:
            ans[a] = sumv % 10
            carry = sumv // 10
        else:
            ans[a] = sumv
        i -= 1
        a -= 1
    else:
        ans[a] = carry

    while j >= 0:
        sumv = arr2[j] + carry
        carry = 0
        if sumv > 9:
            ans[a] = sumv % 10
            carry = sumv // 10
        else:
            ans[a] = sumv
        j -= 1
        a -= 1
    else:
        ans[a] = carry

    return ans

n = int(input())
arr1 = [int(x) for x in input().split()]
m = int(input())
arr2 = [int(x) for x in input().split()]
ans = sumOfTwoArray(arr1, arr2, n, m)
print(*ans)
'''
