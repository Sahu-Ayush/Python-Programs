def UnOrderLinearSearch(arr, n, data):
    for i in range(n):
        if arr[i] == data:
            return i
    return -1

num_ele = int(input())
arr = [int(x) for x in input().split()]
data = int(input())
print(UnOrderLinearSearch(arr, num_ele, data))