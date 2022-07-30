def sort(array):
    odds = sorted([x for x in array if x % 2 != 0], reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in array]


a = [5, 2, 3, 4, 1]
odds = sorted([i for i in a if i % 2 != 0])
c = 0
print(sort(a))
for x in range(len(a)):
    if a[x] % 2 != 0:
        a[x] = odds[c]
        c += 1
