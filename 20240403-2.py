# 덧칠하기(https://school.programmers.co.kr/learn/courses/30/lessons/161989)

def solution(n, m, section):
    answer = 0
    A=[]
    
    for a in range(len(section)):
        A.append(0)

    for b in range(len(section)):
        if A[b]==0:
            A[b]+=1
            answer+=1
            for c in range(b+1,len(section)):
                if section[c]<=section[b]+m-1:
                    A[c]+=1
    
    return answer

B=solution(10,3,[1,3,5,6,8])
C=solution(8,4,[2,3,6])
D=solution(5,4,[1,3])
E=solution(4,1,[1,2,3,4])
print(B,C,D,E)