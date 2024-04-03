# 대충 만든 자판(https://school.programmers.co.kr/learn/courses/30/lessons/160586)

def solution(keymap, targets):
    answer=[]
    A=[]
    for x in range(len(targets)):
        for y in range(len(targets[x])):
            B=[keymap[i].find(targets[x][y])+1 if targets[x][y] in keymap[i] else -1 for i in range(len(keymap)) if targets[x][y] in keymap[i]]
            if B!=[]:
                A.append(min(B))
                B=[]
            else:
                B=[]

        if len(A)==len(targets[x]):
            answer.append(sum(A))
            A=[]
        else:
            answer.append(-1)
            A=[]
    return answer