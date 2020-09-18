# Arrow pattern

'''
Print the following pattern for the given number of rows.
Assume N is always odd.
Note : There is space after every star.


Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*


Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines


Sample Input :
11

Sample Output :
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*
'''

# Code

n = int(input())

i = 1
firsthalf_rows =  n // 2 + 1
secondhalf_rows = n // 2
while i <= firsthalf_rows:
    # Space triangle
    space1 = 1
    while space1 <= i - 1:
#        print("@", end='')
        print(" ", end='')
        space1 += 1
    # Print star (triangle)
    j = 1
    while j <= i:
        print("* ", end='')
        j += 1
    #
    print()
    i += 1

# Printing second half
i = 1
while i <= secondhalf_rows:
    # Space (Inverted triangle)
    space2 = 1
    while space2 <= secondhalf_rows - i:
        # print("@", end='')
        print(" ", end='')
        space2 += 1
    # Inverted triangle
#    j = 1
#    while j <= secondhalf_rows - i + 1:
#       print("* ", end='')
#        j += 1
    j = secondhalf_rows
    while j >= i:
        print("* ", end='')
        j -= 1
    #
    print()
    i += 1
    
    
######################## OR
'''
n=int(input())
inc=(n+1)//2
dec=n-inc
i=1
while i<=inc:
    q=1
    while q<=i-1:
        print(" ",end="") #print("",end="")
        q=q+1
        
        
    j=1
    while j<=i:
        print("* ",end="") #print("*",end="")
        j=j+1
    print()
    i=i+1
i=1
while i<=dec:
    q=1
    while q<=dec-i:
        print(" " ,end="") #print("",end="")
        q=q+1
        
    j=1
    while j<=dec-i+1:
        print("* ",end="") #print("*",end="")
        j=j+1
    print()
    i=i+1
'''
