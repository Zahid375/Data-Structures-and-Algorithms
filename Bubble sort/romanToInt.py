def romanToInt(s):
    sum =0
    romain ={
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    }
    for i in range(0,len(s)):
        print(i)
    return sum


print(romanToInt("CMMXCIV"))