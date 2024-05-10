# 옹알이 (2) (https://school.programmers.co.kr/learn/courses/30/lessons/133499?language=python3)

def solution(babbling):
    b = ["aya", "ye", "woo", "ma"]
    bb = ["ayaaya","yeye","woowoo","mama"]

    for i in range(len(b)):
        for j in range(len(babbling)):
            if bb[i] not in babbling[j]:
                babbling[j] = babbling[j].replace(b[i],"")

    answer = babbling.count("")

    return answer

A=solution(["aya", "yee", "u", "maa"])
B=solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])

print(A,B)