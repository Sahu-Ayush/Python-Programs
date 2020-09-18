# Largest Row or Column

'''
For a given two-dimensional integer array/list of size (N x M),
you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.

Note :
If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.


Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.

Output Format :
For each test case, If row sum is maximum, then print: "row" <row_index> <row_sum>
OR
If column sum is maximum, then print: "column" <col_index> <col_sum>
It will be printed in a single line separated by a single space between each piece of information.

Output for every test case will be printed in a seperate line.

Consider :
If there doesn't exist a sum at all then print "row 0 -2147483648", where -2147483648 or -2^31 is the smallest value for the range of Integer.


Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= M <= 10^3
Time Limit: 1sec


Sample Input 1 :
1
2 2 
1 1 
1 1

Sample Output 1 :
row 0 2


Sample Input 2 :
2
3 3
3 6 9 
1 4 7 
2 8 9
4 2
1 2
90 100
3 40
-10 200

Sample Output 2 :
column 2 25
column 1 342
'''

# Code

from sys import stdin

MIN_VALUE = -2147483648
def findLargest(arr, nRows, mCols):

    isRow = True
    largestSum = MIN_VALUE
    num = 0

    for i in range(nRows):
        rowSum = 0
        for j in range(mCols):
            rowSum += arr[i][j]

        if rowSum > largestSum:
            largestSum = rowSum
            num = i

    for j in range(mCols):
        colSum = 0
        for i in range(nRows):
            colSum += arr[i][j]
        
        if colSum > largestSum:
            largestSum = colSum
            num = j
            isRow = False

    if isRow:
        print("row " + str(num) + " " + str(largestSum))
    else:
        print("column " + str(num) + " " + str(largestSum))


#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1

### OR ####

'''
def largestRowCol(arr):
    n = len(arr)
    m = len(arr[0])
    max_row_sum = -1
    max_row_index = -1
    for i in range(n):
        sum = 0
        for ele in arr[i]:
            sum += ele
        if sum > max_row_sum:
            max_row_sum = sum
            max_row_index = i

    max_col_sum = -1
    max_col_index = -1
    for j in range(m):
        sum = 0
        for ele in arr:
            sum += ele[j]
        if sum > max_col_sum:
            max_col_sum =sum
            max_col_index = j

    if max_col_sum > max_row_sum:
		# print("col ", max_col_index, max_col_sum)
        return "column", max_col_index, max_col_sum
    else:
		# print("row ", max_row_index, max_row_sum)
        return "row", max_row_index, max_row_sum


#Main
m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
l=largestRowCol(arr)
print(*l)
'''
