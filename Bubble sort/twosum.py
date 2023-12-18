def twoSum(num,target):
    for i in range(0,len(num)-1):
        for j in range(i+1,len(num)):
            if(num[i]+num[j] == target):
                return [i,j]
    return False


num = [2,5,5,11]
target = 10

print(twoSum(num,target))