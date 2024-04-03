# 바탕화면 정리(https://school.programmers.co.kr/learn/courses/30/lessons/161990)

def solution(wallpaper):
    answer = [0,0,0,0]
    
    for a in range(len(wallpaper)):
        if "#" in wallpaper[a]:
            break
        else:
            answer[0]+=1

    for b in range(len(wallpaper[0])):
        if "#" in [B[b] for B in wallpaper]:
            break
        else:
            answer[1]+=1

    for c in range(answer[0],len(wallpaper)):
        if "#" in wallpaper[c]:
            answer[2]=c+1

    for d in range(answer[1],len(wallpaper[0])):
        if "#" in [D[d] for D in wallpaper]:
            answer[3]=d+1
    
    return answer