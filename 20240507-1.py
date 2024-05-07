# 기사단원의 무기(https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=python3)

def solution(number, limit, power):
    answer = 0
    l=[0]*(number+1)
    for i in range(1,number+1):
        for j in range(0,number+1,i):
            l[j]+=1
    for k in range(1,len(l)):
        if l[k]>limit:
            answer+=power
        else:
            answer+=l[k]
    return answer