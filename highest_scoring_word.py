def high(x):
    words = x.split()
    mx = max(words, key=lambda k: sum(ord(c) - 96 for c in k))
    return mx


def high2(x):
    record = []
    words = x.split()
    for i in words:
        record.append(sum(ord(y) - 96 for y in i))
    return words[record.index(max(record))]


print(high2("Hello there"))
