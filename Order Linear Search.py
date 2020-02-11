# Array must be sorted

def OrderLinearSearch(arr, n, data):
    for i in range(n):
        if arr[i] == data:
            return i
        elif arr[i] > data:
            return -1
    return -1

num_ele = int(input())
arr = [int(x) for x in input().split()]
data = int(input())
print(OrderLinearSearch(arr, num_ele, data))