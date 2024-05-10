# 옹알이 (2) (https://school.programmers.co.kr/learn/courses/30/lessons/133499?language=python3)

def solution(babbling):
    answer = 0
    b = ["aya", "ye", "woo", "ma"]
    bb = ["ayaaya","yeye","woowoo","mama"]

    for i in range(len(babbling)):
        for j in range(len(b)):
            if bb[j] not in babbling[i]:
                babbling[i] = babbling[i].replace(b[j],"B")
        if babbling[i].count("B") == len(babbling[i]):
            answer += 1

    return answer