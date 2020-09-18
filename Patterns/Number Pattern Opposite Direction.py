# Number Pattern

'''
Print the following pattern for n number of rows.
For eg. N = 5

1        1
12      21
123    321
1234  4321
1234554321


Sample Input 1 :
4

Sample Output 1 :
1      1
12    21
123  321
12344321
'''

# Code

n = int(input())
d = n - 1
i = 1
while i <= n:
    # Increasing number (right triangle)
    j = 1
    while j <= i:
        print(j, end='')
        j += 1
    # Space (in Inverted triangle order)
    space = 1
    while space <= n - i + d:
#        print("@", end='')
        print(" ", end='')
        space += 1
    # Increasing number (Mirror Image)
    p = i
    while p >= 1:
        print(p, end='')
        p -= 1
    #
    print()
    i += 1
    d -= 1
