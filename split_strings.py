def solution(s):
    if len(s) % 2 == 0:
        return list((s[i] + s[i + 1] for i in range(0, len(s), 2)))
    else:
        s = s + "_"
        return list((s[i] + s[i + 1] for i in range(0, len(s), 2)))


print(solution("asdfadsf"))
print(solution("asdfads"))
