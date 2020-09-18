# Check Armstrong

'''
Write a Program to determine if the given number is Armstrong number or not.
Print true if number is armstrong, otherwise print false.

An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.


For example,
371, as 3^3 + 7^3 + 1^3 = 371
1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634


Input Format :
Integer n

Output Format :
true or false


Sample Input 1 :
1

Sample Output 1 :
true


Sample Input 2 :
103

Sample Output 2 :
false
'''

# Code

def power(base, n):
    power = 1
    for x in range(1, n + 1):
        power = power * base
    return power

def checkArmstrong (n):
    checkNum = n
    count = 0

    while checkNum > 0:
        rem = checkNum % 10
        checkNum //= 10
        count += 1
    power_d = count
    # print("power_d", power_d)
    
    checkNum = n
    armstrongPower = 0

    while checkNum > 0:
        base_d = checkNum % 10
        # print("base_d", base_d)
        armstrongPower = armstrongPower + power(base_d, power_d)
        # print("armstrongPower", armstrongPower)
        checkNum //= 10
    # print(armstrongPower, " ", n)
    return armstrongPower == n

# Driver Code
n = int(input())
nIsArmstrong = checkArmstrong(n)
if nIsArmstrong:
    print("true")
else:
    print("false")

### OR ###

'''
def checkArmstrong(n):
    digits = 0
    num = n
    while num > 0:
        digits += 1
        num //=10
    newNum = 0
    num = n

    while num > 0:
        last = num%10
        newNum = newNum + (last**digits)
        num //= 10
    if newNum == n:
        return True
    else:
        return False

n = int(input())
nIsArmstrong = checkArmstrong(n)
if nIsArmstrong:
    print("true")
else:
    print("false")
'''
