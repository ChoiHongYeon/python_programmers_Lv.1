# 자릿수 더하기 (https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=python3)

def solution(n):

    answer = 0
    s = str(n)
    for i in range(len(s)):
        answer += int(s[i])

    return answer

print(solution(123))
print(solution(987))