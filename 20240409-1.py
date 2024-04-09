# 문자열 나누기(https://school.programmers.co.kr/learn/courses/30/lessons/140108)

def solution(s):
    answer=0
    A=0
    B=s[0]
    C=[]
    D=0
    if len(s)!=1:
        for i in range(2,len(s)):
            if s[A:i].count(B)==(i-A)/2:
                C.append(s[A:i])
                A=i
                B=s[i]
        for i in range(len(C)):
            D+=len(C[i])
        if len(s)==D:
            answer=len(C)
        else:
            answer=len(C)+1
    else:
        answer=1
    return answer