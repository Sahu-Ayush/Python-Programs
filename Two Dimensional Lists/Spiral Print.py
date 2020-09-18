# Spiral Print

'''
For a given two-dimensional integer array/list of size (N x M), print it in a spiral form.
That is, you need to print in the order followed for every iteration:
a. First row(left to right)
b. Last column(top to bottom)
c. Last row(right to left)
d. First column(bottom to top)

Mind that every element will be printed only once.
Refer to the Image:



Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.

Output format :
For each test case, print the elements of the two-dimensional array/list in the spiral form in a single line, separated by a single space.

Output for every test case will be printed in a seperate line.


Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= M <= 10^3
Time Limit: 1sec


Sample Input 1:
1
4 4 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16

Sample Output 1:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 


Sample Input 2:
2
3 3 
1 2 3 
4 5 6 
7 8 9
3 1
10
20
30

Sample Output 2:
1 2 3 6 9 8 7 4 5 
10 20 30
'''

# Code

from sys import stdin

def spiralPrint(mat, nRows, mCols):

    if nRows==0:
        return

    rowStart, colStart = 0, 0

    numElements = nRows * mCols
    count = 0

    while count < numElements:
        i = colStart
        while i < mCols and count < numElements:
            print(mat[rowStart][i], end=" ")
            count += 1
            i += 1

        rowStart += 1

        i = rowStart
        while i < nRows and count < numElements:
            print(mat[i][mCols-1], end=" ")
            count += 1
            i += 1

        mCols -= 1

        i = mCols-1
        while i >= colStart and count < numElements:
            print(mat[nRows-1][i], end=" ")
            count += 1
            i -= 1

        nRows -= 1

        i = nRows-1
        while i >= rowStart and count < numElements:
            print(mat[i][colStart], end=" ")
            count += 1
            i -= 1

        colStart += 1


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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1

### OR ###


'''
def spiralPrint(arr):
    # Please add your code here
    # pass
    m = len(arr)
    n = len(arr[0])
    k = 0;
    l = 0
    spiral_arr = []
    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            # print(arr[k][i], end=" ")
            spiral_arr.append(arr[k][i])

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            # print(arr[i][n - 1], end=" ")
            spiral_arr.append(arr[i][n - 1])

        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                # print(arr[m - 1][i], end=" ")
                spiral_arr.append(arr[m - 1][i])

            m -= 1

        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                # print(arr[i][l], end=" ")
                spiral_arr.append(arr[i][l])

            l += 1
    return spiral_arr

#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
arr = spiralPrint(arr)
print(*arr)
'''


'''
Approach:
The problem can be solved by dividing the matrix into loops or squares or boundaries.
It can be seen that the elements of the outer loop are printed first in a clockwise manner then
the elements of the inner loop is printed.
So printing the elements of a loop can be solved using four loops which prints all the elements.
Every ‘for’ loop defines a single direction movement along with the matrix.
The first for loop represents the movement from left to right,
whereas the second crawl represents the movement from top to bottom,
the third represents the movement from the right to left,
and the fourth represents the movement from bottom to up.

Algorithm:
1) create and initilize variables k – starting row index, m – ending row index,
l – starting column index, n – ending column index

2) Run a loop until all the squares of loops are printed.
In each outer loop traversal print the elements of a square in clockwise manner.

3) Print the top row, i.e. Print the elements of kth row from column index l to n,
and increase the count of k.

4) Print the right column, i.e. Print the last column or n-1th column from row index k to m
and decrease the count of n.

5) Print the bottom row, i.e. if k > m, then print the elements of m-1th row
from column n-1 to l and decrease the count of m

6) Print the left column, i.e. if l < n, then print the elements of lth column
from m-1th row to k and increase the count of l.
'''
