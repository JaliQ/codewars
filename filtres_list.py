def filter_list(l):
    filt = [l[i] for i in range(len(l)) if type(l[i]) is int]
    return filt


print(filter_list([1, 2, 3, "A", "BC"]))
