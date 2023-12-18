def binarySearch(arr, target):
    start = 0
    end = len(arr)-1
    while (start <= end):
        mid = abs(int((start+end)/2))
        if (target < arr[mid]):
            end = mid-1
        elif (target > arr[mid]):
            start = mid+1
        else:
            return mid
    return False


arr = [2, 3, 5, 5, 6, 10, 34, 56, 100]

target = 5

result = binarySearch(arr, target)
print(result)
