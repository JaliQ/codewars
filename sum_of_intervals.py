def sum_of_intervals(intervals):
    res = 0
    used = []
    for i in intervals:
        for j in range(i[0], i[1]):
            if j not in used:
                res += 1
                used.append(j)

    return res


print(sum_of_intervals([(1, 5)]))
