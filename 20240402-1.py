# 추억 점수(https://school.programmers.co.kr/learn/courses/30/lessons/176963)

def solution(name, yearning, photo):
    answer = []
    dic=dict(zip(name,yearning))
    for i in range(len(photo)):
        answer.append(sum([dic[a] if a in name else 0 for a in photo[i]]))
    return answer