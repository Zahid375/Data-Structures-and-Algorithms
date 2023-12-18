def NumberOfDigit(n):
    if (n == 0):
        return 0

    return n % 10 + NumberOfDigit(int(n/10))


print(NumberOfDigit(1234))
