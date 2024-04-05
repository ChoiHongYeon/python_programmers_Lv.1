# 가장 가까운 같은 글자(https://school.programmers.co.kr/learn/courses/30/lessons/142086)

def solution(s):
    answer = [-1]
    if len(s)!=1:
        for a in range(1,len(s)):
            if s[a] not in s[0:a]:
                answer.append(-1)
            else:
                for b in range(a-1,-1,-1):
                    if s[a]==s[b]:
                        answer.append(a-b)
                        break
    return answer