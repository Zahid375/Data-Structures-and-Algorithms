def selectionSort(arr):
    for i in range(0, len(arr)):
        lastIndex = len(arr)-i-1
        maxIndex = maxArrayIndex(arr, 0, lastIndex)
        swapArrayelement(arr, lastIndex, maxIndex)

    return arr


def maxArrayIndex(arr, start, end):
    max = start
    for j in range(start, end+1):
        if (arr[max] < arr[j]):
            max = j
    return max


def swapArrayelement(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


arr = [3, 2, 1, 5, 3, 6]

result = selectionSort(arr)

print(result)
