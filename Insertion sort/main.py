def insertionSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,0,-1):
            if(arr[j]>arr[j-1]):
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            else:
                break
    return arr


arr = [43,2,34,64,32,4]

result = insertionSort(arr)

print(arr)
