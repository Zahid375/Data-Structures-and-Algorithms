
def isBalance(value):
    stack = []
    for i in range(len(value)):
        if value[i] == '{' or value[i] == '[' or value[i] == '(':
            stack.append(value[i])
        elif value[i] == '}' or value[i] == ']' or value[i] == ')':
            if (issame(stack[-1], value[i]) or len(stack) != 0):
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


def issame(first, last):
    if '{' == first and '}' == last:
        return True
    if '(' == first and ')' == last:
        return True
    if '[' == first and ']' == last:
        return True
    return False


print(isBalance("{[2(x+y)]^2}10"))
