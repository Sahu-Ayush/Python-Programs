# Zeros and Stars Pattern

'''
Print the following pattern


Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000


Input Format :
N (Total no. of rows)

Output Format :
Pattern in N lines


Sample Input 1 :
3

Sample Output 1 :
*00*00*
0*0*0*0
00***00


Sample Input 2 :
5

Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
'''

# Code

n = int(input())

i = 1
while i <= n:  #this loop is used to print n
    ######
    j = 1
    while j <= n:      #this loop is used to print n
        if i == j:
            print("*", end='')
        else:
            print("0", end='')
        j = j + 1
    ######
    j = j - 1;
    print("*", end='')
    while j >= 1:  #this loop is used to print n
        if i == j:
            print("*", end='')
        else:
            print("0", end='')
        j = j - 1
    print();
    i = i + 1
