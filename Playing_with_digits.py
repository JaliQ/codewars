def dig_pow(n, p):
    num = 0
    for i, c in enumerate(str(n)):
        num += pow(int(c), p + i)
    return num // n if num % n == 0 else -1


print(dig_pow(89, 1))
