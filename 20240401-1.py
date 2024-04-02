# 달리기 경주(https://school.programmers.co.kr/learn/courses/30/lessons/178871)

def solution(players, callings):
    players_dict={player:i for i,player in enumerate(players)}
    for calling in callings:
        x=players_dict[calling]-1
        y=players_dict[calling]
        players_dict[players[x]]=y
        players_dict[players[y]]=x
        players[x],players[y]=players[y],players[x]
    return players