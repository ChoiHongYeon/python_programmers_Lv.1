# 덧칠하기(https://school.programmers.co.kr/learn/courses/30/lessons/161989)

def solution(n, m, section):
    answer = 0
    A=[]
    
    for a in range(n+m):
        A.append(0)

    for b in range(len(section)):
        if A[section[b]]==0:
            A[section[b]]+=1
            answer+=1
            for c in range(1,m):
                A[section[b]+c]+=1

    return answer