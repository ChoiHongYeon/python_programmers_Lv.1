# 콜라 문제(https://school.programmers.co.kr/learn/courses/30/lessons/132267)

def solution(a, b, n):
    answer = 0

    while n >= a:
        answer += (int(n / a) * b)
        n = n - (n - (n % a)) + (int(n / a) * b)

    return answer