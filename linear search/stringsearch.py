def linear_search(arr, target):
    for i in range(0, len(arr)):
        if (arr[i] == target):
            return [i, arr[i]]
    else:
        return -1


name = "zahidul islam"

target = 'u'

result = linear_search(name, target)
