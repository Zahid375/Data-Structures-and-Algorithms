def binaryWithRecursion(arr, target, start, end):
    if (start > end):
        return False

    mid = int((start+end)/2)

    if (target < arr[mid]):
        return binaryWithRecursion(arr, target, 0, mid-1)
    elif (target > arr[mid]):
        return binaryWithRecursion(arr, target, mid+1, end)
    else:
        return mid


arr = [23, 43, 21, 4, 63, 2, 34]
arr.sort()
target = 21

print(binaryWithRecursion(arr, target, 0, len(arr)-1))
