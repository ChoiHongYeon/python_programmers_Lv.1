# 카드 뭉치(https://school.programmers.co.kr/learn/courses/30/lessons/159994)

def solution(cards1, cards2, goal):
    answer = 'Yes'
    A=[]
    B=[]
    
    for i in range(len(goal)):
        if goal[i] in cards1:
            A.append(goal[i])
        elif goal[i] in cards2:
            B.append(goal[i])

    if len(A)>1:
        for a in range(len(A)):
            if cards1[a]!=A[a]:
                answer='No'
    
    if len(B)>1:
        for b in range(len(B)-1):
            if cards2[b]!=B[b]:
                answer='No'

    return answer