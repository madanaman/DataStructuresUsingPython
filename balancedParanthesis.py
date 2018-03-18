from Stack import Stack

def parenChecker(ip_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(ip_string) and balanced:
        symbol = ip_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parenChecker('((()))'))
print(parenChecker('(()'))

