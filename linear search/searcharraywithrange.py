def linearSearchWithrange(arr, start, end):
    arr_len = len(arr)
    if (arr_len > start and arr_len > end):
        arr2 = []
        for i in range(start, end):
            arr2.append(arr[i])
        return arr2
    else:
        return False


arr = [23, 42, 53, -2, 53, 0, 4, -93, 0.34]

start = 1
end = 3
result = linearSearchWithrange(arr, start, end)

print(result)
