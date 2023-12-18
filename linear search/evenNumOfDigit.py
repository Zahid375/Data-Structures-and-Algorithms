import math
nums = [12, 43, 333333, 345, 2, 6, 7896]


def findDigit(num):
    return len(str(num))


def findEven(num):
    if (num % 2 == 0):
        return True
    return False


def find(nums):
    count = 0
    for i in range(0, len(nums)):
        if (findEven(findDigit(nums[i]))):
            count += 1
    return count


result = find(nums)

print(result)
