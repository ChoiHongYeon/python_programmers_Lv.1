# 달리기 경주(https://school.programmers.co.kr/learn/courses/30/lessons/178871)

def solution(players, callings):
    players_dict={player:i for i,player in enumerate(players)}
    players_num=list(range(len(players)))
    callings_num=[players_dict[calling] for calling in callings]

    for x in range(len(callings_num)):
        y=players_num.index(callings_num[x])
        players_num[y],players_num[y-1]=players_num[y-1],players_num[y]

    answer=[players[j] for j in players_num]
    return answer