def bubble(arr):
    for i in range(0,len(arr)):
        for j in range(1,len(arr)-i):
            if(arr[j]<arr[j-1]):
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    return arr


def bubbleMoreEfficent(arr):
    isSwap = False
    for i in range(0,len(arr)):
        for j in range(1,len(arr)-1):
            if(arr[j]<arr[j-1]):
                isSwap = True
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
        if(isSwap == False):
            break
    return arr

arr = [1,2,3,4,5]

result = bubbleMoreEfficent(arr)
print(result)
