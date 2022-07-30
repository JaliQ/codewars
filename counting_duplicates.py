from string import ascii_letters


def duplicate_count(text):
    av = ascii_letters + "0123456789"
    c = [text.count(k) for k in av]
    l = [c[i] + c[i + 26] for i in range(26)]
    n = [c[i] for i in range(52, 62)]
    return (len(l) - (l.count(0) + l.count(1))) + (len(n) - (n.count(0) + n.count(1)))


def perfect_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


print(perfect_count("AASSZ"))
