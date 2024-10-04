# 문자열 내 마음대로 정렬하기 (https://school.programmers.co.kr/learn/courses/30/lessons/12915?language=python3)

def solution(strings, n):

    strings.sort()
    strings = sorted(strings, key = lambda x : x[n])

    return strings

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))