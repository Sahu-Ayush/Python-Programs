# Pyramid Number Pattern

'''
Print the following pattern for the given number of rows.

Pattern for N = 4
   1
  212
 32123
4321234


Input format : N (Total no. of rows)

Output format : Pattern in N lines


Sample Input :
5

Sample Output :
    1
   212
  32123
 4321234
543212345
'''

# Code

n = int(input())

i = 1
while i <= n:
    # Space (Inverted)
    space = 1
    while space <= n - i:
        #print("@", end='')
        print(" ", end='')
        space += 1
    #Printing numbers
    j = 1
    no_print = i
    while j <= i:
        print(no_print, end='')
        no_print -= 1
        j += 1
    # Printing second half
    p = 2
    while p <= i:
        print(p, end='')
        p += 1
    #
    print()
    i += 1
   
   #### OR
   '''
   n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end='')
    end=i
    for k in range(i,0,-1):
        print(i,end='')
        i-=1
    
    for j in range(2, end+1):
        print(j,end='')       
    i+=1   
    print()
'''
