# Print the pattern

'''

'''

# Code

n = int(input())

first_half_n = 0
second_half_n = n // 2
start_j = 1

if n % 2 == 0:
    first_half_n = n // 2
else:
    first_half_n = (n // 2) + 1

# Printing first n // 2 rows if n is even else n // 2 + 1
for i in range(1, first_half_n + 1):
    #
    for j in range(start_j, start_j + n):
        print(j, end=' ')
    else:
        start_j = j + n + 1
    #
    # print("=", j, end='')
    print()

# Printing last n // 2 rows
if n % 2 == 0:
        start_j = j + 1
else:
        start_j = j - ( 2 * n) + 1
for i in range(1, second_half_n + 1):
    #
    for j in range(start_j, start_j + n):
        print(j, end=' ')
    else:
        start_j = j - (3 * n) + 1
    #
    print()
