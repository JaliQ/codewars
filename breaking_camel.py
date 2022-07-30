def solution(s):
    return "".join(i if not i.isupper() else " " + i for i in s)


print(solution("helloWorld"))
