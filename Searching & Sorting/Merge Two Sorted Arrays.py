# Merge Two Sorted Arrays

'''
You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively,
merge them into a third array/list such that the third array is also sorted.


Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements of the first array/list.

Third line contains an integer 'M' representing the size of the second array/list.

Fourth line contains 'M' single space separated integers representing the elements of the second array/list.

Output Format :
For each test case, print the sorted array/list(of size N + M) in a single row, separated by a single space.

Output for every test case will be printed in a separate line.


Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
0 <= M <= 10^5
Time Limit: 1 sec 
'''

# Code

from sys import stdin

def merge(arr1, n, arr2, m):
    ans=(n+m) * [0]
    i = 0
    j = 0
    k = 0
    while i < n and j < m:
        if  arr1[i] < arr2[j]:
            ans[k] = arr1[i]
            k += 1
            i += 1
        else:
            ans[k] = arr2[j]
            k += 1
            j += 1

    while i < n:
        ans[k] = arr1[i]
        k += 1
        i += 1

    while j < m:
        ans[k] = arr2[j]
        k += 1
        j += 1

    return ans

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1

### OR ###

'''
def mergeSortedArray1(arr1, arr2, n, m):
    i = 0
    j = 0
    arr = []
    while (i < n) and (j < m):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while i < n:
        arr.append(arr1[i])
        i += 1
    while j < m:
        arr.append(arr2[j])
        j += 1
    return arr

n = int(input())
arr1 = [int(x) for x in input().split()]
m = int(input())
arr2 = [int(x) for x in input().split()]
arr = mergeSortedArray1(arr1, arr2, n, m)
print(' '.join([str(x) for x in arr]))
'''
