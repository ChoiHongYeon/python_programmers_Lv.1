# 문자열을 정수로 바꾸기 (https://school.programmers.co.kr/learn/courses/30/lessons/12925?language=python3)

def solution(s):
    
    return int(s) if s[0] != "-" else int(s[1:]) * -1

print(solution("1234"))
print(solution("-1234"))