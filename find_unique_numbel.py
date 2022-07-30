def find_uniq(arr):
    arr.sort()
    return arr[0] if arr.count(arr[0]) == 1 else arr[-1]
