# Find maximum value in List

##def minVal(lst):
##    min = lst[0]
##
##    for i in range(1, len(lst)):
##        if lst[i] < min:
##            min = lst[i]
##    return min


def maxVal(lst):
    max = lst[0]

    for ele in lst:
        if ele > max:
            max = ele
    return max



# Main
lst = [int(ele) for ele in  input().split()]
print(maxVal(lst))
