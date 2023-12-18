def missingNumber(arr):
    i = 0
    while(i<len(arr)):
        index = arr[i]
        if(arr[i] < len(arr) and arr[i] != arr[index]):
            temp = arr[index]
            arr[index] = arr[i]
            arr[i] = temp
        else:
            i=i+1

    for j in range(0,len(arr)):
        if(arr[j] != j):
            return j

    return len(arr)



arr = [4,0,2,1]

print(missingNumber(arr))



