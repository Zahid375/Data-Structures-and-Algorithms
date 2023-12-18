def oneToN(n):
    # base condition
    if (n == 0):
        return
    print(n)
    # Recustion function call here.
    oneToN(n-1)
    print(n)


oneToN(5)
