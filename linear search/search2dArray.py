def search2dArray(arr, target):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if (arr[i][j] == target):
                return [i, j]

    return False


arr = [[1, 3, 4], [44, 53, 23,], [42, 63, 63]]

target = 42

result = search2dArray(arr, target)

print(result)
