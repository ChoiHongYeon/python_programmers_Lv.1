# 공원 산책(https://school.programmers.co.kr/learn/courses/30/lessons/172928)

def solution(park, routes):
    answer=[0,0]
    sub=[]

    for a in range(len(park)):
        if "S" in park[a]:
            answer[0]=a
        for b in range(len(park[0])):
            if park[a][b]=="S":
                answer[1]=b

    route_A=[route[0] for route in routes]
    route_B=[int(route[2]) for route in routes]

    for x in range(len(routes)):
        if route_A[x]=="E":
            for y in range(answer[1]+1,answer[1]+route_B[x]):
                if park[answer[0]][y]=="X":
                    sub.append("NO")
            if 0<=answer[1]+route_B[x]<=len(park[0])-1 and "NO" not in sub:
                answer[1]+=route_B[x]
                sub=[]
            else:
                sub=[]
        elif route_A[x]=="W":
            for y in range(answer[1]-route_B[x],answer[1]-1):
                if park[answer[0]][y]=="X":
                    sub.append("NO")
            if 0<=answer[1]-route_B[x]<=len(park[0])-1 and "NO" not in sub:
                answer[1]-=route_B[x]
                sub=[]
            else:
                sub=[]
        elif route_A[x]=="S":
            for y in range(answer[0]+1,answer[0]+route_B[x]):
                if park[y][answer[1]]=="X":
                    sub.append("NO")
            if 0<=answer[0]+route_B[x]<=len(park)-1 and "NO" not in sub:
                answer[0]+=route_B[x]
                sub=[]
            else:
                sub=[]
        elif route_A[x]=="N":
            for y in range(answer[0]-route_B[x],answer[0]-1):
                if park[y][answer[1]]=="X":
                    sub.append("NO")
            if 0<=answer[0]-route_B[x]<=len(park)-1 and "NO" not in sub:
                answer[0]-=route_B[x]
                sub=[]
            else:
                sub=[]

    return answer