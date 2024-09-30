# 문자열 내 p와 y의 개수 (https://school.programmers.co.kr/learn/courses/30/lessons/12916?language=python3)

def solution(s):

    p = 0
    y = 0
    for i in s:
        if i == 'p' or i == 'P':
            p += 1
        if i == 'y' or i == 'Y':
            y += 1

    return p == y

print(solution("pPoooyY"))
print(solution("Pyy"))