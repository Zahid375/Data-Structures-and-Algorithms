def linear_search(arr, target):
    for i in range(0, len(arr)):
        if (arr[i] == target):
            return [i, arr[i]]
    else:
        return -1


arr = [23, 42, 53, -2, 53, 0, 4, -93, 0.34]

target = 0.34

result = linear_search(arr, target)

print(f"index = {result[0]} |  value  = {result[1]}")
