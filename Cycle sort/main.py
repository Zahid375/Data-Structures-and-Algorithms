def CycleSort(arr):
    i= 0
    while(i<len(arr)):
        index = arr[i]-1
        if(arr[index]!=arr[i]):
            temp = arr[index]
            arr[index] = arr[i]
            arr[i] = temp
        else:
            i=i+1
    return arr


arr=[3,4,1,2,5]

print(CycleSort(arr))