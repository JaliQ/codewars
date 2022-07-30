def max_sequence(arr):
    maxSum = 0
    currentSum = 0
    for i in arr:
        currentSum += i
        if maxSum < currentSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum
