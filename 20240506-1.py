# 명예의 전당 (1) (https://school.programmers.co.kr/learn/courses/30/lessons/138477?language=python3)

def solution(k, score):
    answer = []
    A=[]
    for i in range(len(score)):
        if i<k:
            A.append(score[i])
            answer.append(min(A))
        else:
            A.sort()
            if score[i]>A[0]:
                A[0]=score[i]
            answer.append(min(A))
    return answer