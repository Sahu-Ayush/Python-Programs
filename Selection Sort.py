def SelectionSort(arr, n):
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

num_ele = int(input())
arr = [int(x) for x in input().split()]
print(SelectionSort(arr, num_ele))