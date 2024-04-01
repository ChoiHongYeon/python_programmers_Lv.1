# 달리기 경주(https://school.programmers.co.kr/learn/courses/30/lessons/178871)

def solution(players, callings):
    answer = []
    players_dict={player:i for i,player in enumerate(players)}
    players_number=list(players_dict.values())
    callings_number=[players_dict[calling] for calling in callings]
    
    for x in range(len(callings_number)):
        for y in range(1,len(players_number)):
            if callings_number[x]==players_number[y]:
                players_number[y-1],players_number[y]=players_number[y],players_number[y-1]

    for i in range(len(players_number)):
        answer.append(players[players_number[i]])
    
    return answer

A=solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])
print(A)