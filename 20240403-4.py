# 카드 뭉치(https://school.programmers.co.kr/learn/courses/30/lessons/159994)

def solution(cards1, cards2, goal):
    answer = 'Yes'
    for a in range(len(cards1)-1):
        if goal.index(cards1[a+1])<goal.index(cards1[a]):
            answer='No'  
    for b in range(len(cards2)-1):
        if goal.index(cards2[b+1])<goal.index(cards2[b]):
            answer='No'
    return answer

A=solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"])
B=solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"])
print(A,B)