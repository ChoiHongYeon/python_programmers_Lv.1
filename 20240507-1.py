# 기사단원의 무기https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=python3)

def solution(number, limit, power):
    answer = 0
    l=[0]*(number+1)
    for i in range(1,number+1):
        for j in range(1,i+1):
            if l[i]>limit: break
            if i%j==0:
                l[i]+=1
    for k in range(len(l)):
        if l[k]>limit:
            answer+=power
        else:
            answer+=l[k]
    return answer

A=solution(5,3,2)
B=solution(10,3,2)
print(A,B)