# 햄버거 만들기(https://school.programmers.co.kr/learn/courses/30/lessons/133502)

def solution(H):
    answer = 0
    for i in range(len(H)):
        if H[i] == 1:
            if i+3 <= len(H) and H[i+1] == 2 and H[i+2] == 3 and H[i+3] == 1:
                answer += 1
                del H[i:i+4]
                H[0:0] = [0,0,0,0]
    return answer
   
A = solution([2,1,1,2,3,1,2,3,1])
B = solution([1,3,2,1,2,1,3,1,2])
print(A,B)