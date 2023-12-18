def Nto1(n):
    # base condition
    if (n == 0):
        return
    print(n)
    # Recustion function call here.
    return Nto1(n-1)


Nto1(5)
