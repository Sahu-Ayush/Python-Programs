def isArrayInSortedOrder(lst):
    if len(lst) == 1:
        return True
    return (lst[0] < lst[1]) and isArrayInSortedOrder(lst[1:])


lst = list(map(int, input().split()))
print(isArrayInSortedOrder(lst))