def orderAcnosticBs(arr, target):
    start = 0
    end = len(arr)-1

    def isAsending():
        if (arr[start] < arr[end]):
            return True
        return False
    while (start <= end):
        mid = int(start+(end-start)/2)
        if (isAsending()):
            if (target < arr[mid]):
                end = mid - 1
            elif (target > arr[mid]):
                start = mid+1
            else:
                return mid
        else:
            if (target > arr[mid]):
                end = mid - 1
            elif (target < arr[mid]):
                start = mid+1
            else:
                return mid

    return False


array1 = [2, 4, 6, 7, 23, 53, 64, 560]
array2 = [342, 332, 52, 3, 0, -42]

result = orderAcnosticBs(array2, 0)
print(result)
