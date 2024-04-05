# 크기가 작은 부분문자열(https://school.programmers.co.kr/learn/courses/30/lessons/147355)

def solution(t, p):
    answer = 0
    for i in range(0,len(t)-len(p)+1):
        if t[i]!=0 and int(t[i:i+len(p)])<=int(p):
            answer+=1
    return answer