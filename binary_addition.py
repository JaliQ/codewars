def add(x1, x2):
    if (type(x1) is int) and (type(x2) is int):
        s = bin(x1 + x2)[2:]
        return s
    else:
        return "Type Error"
