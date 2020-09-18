'''
WAP to print the given below pattern

N = 4
$ $ $ $ $ $ $
  * * * * *
    $ $ $
      *
# OR

N = 4
N N N N N N N
  C C C C C
    N N N
      C
'''








# Code

n = int(input())

# Print character
for row in range(n, 0, -1):

    space = 2*(n-row)
    while space > 0:
        print(end=" ")
        space -= 1

    char_print_count = 2*row-1

    #while char_print_count >= 1:
    for _ in range(char_print_count, 0, -1):
        if row%2 == 0:
            #print("$", end="")
            print("N", end="")
            #if char_print_count != 1:
            if _ != 1:
                print(end=" ")
        else:
            #print("*", end="")
            print("C", end="")
            #if char_print_count != 1:
            if _ != 1:
                print(end=" ")
                
        #char_print_count -= 1
    print()
