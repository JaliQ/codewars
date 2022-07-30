def prime_factors(n):
    numbers = {}
    d = 1
    if n == 1:
        return 1
    while n > 1:
        d += 1
        if n % d == 0:
            numbers[d] = 0
            while n % d == 0:
                numbers[d], n = numbers[d] + 1, n // d
    return "".join(
        f"({key}**{items})" if items > 1 else f"({key})"
        for key, items in numbers.items()
    )


print(prime_factors(7919))
