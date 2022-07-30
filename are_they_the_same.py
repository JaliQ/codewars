def comp(a1, a2):
    try:
        return sorted([i ** 2 for i in a1]) == sorted(a2)
    except:
        return False
