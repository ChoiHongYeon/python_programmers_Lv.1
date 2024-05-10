# 햄버거 만들기(https://school.programmers.co.kr/learn/courses/30/lessons/133502)

def solution(H):
    answer = 0
   
    for i in range(len(H)):
        if i >= 0 and i + 3 <= len(H):
            if H[i] == 1 and H[i + 1] == 2 and H[i + 2] == 3 and H[i + 3] == 1:
                answer += 1
                for i in range(4):
                    H.pop(i)
        elif i >= 1 and i + 2 <= len(H):
            if H[i - 1] == 1 and H[i] == 2 and H[i + 1] == 3 and H[i + 2] == 1:
                answer += 1
                for i in range(4):
                    H.pop(i - 1)
        elif i >= 2 and i + 1 <= len(H):
            if H[i - 2] == 1 and H[i - 1] == 2 and H[i] == 3 and H[i + 1] == 1:
                answer += 1
                for i in range(4):
                    H.pop(i - 2)
        elif i >= 3 and i <= len(H):
            if H[i - 3] == 1 and H[i - 2] == 2 and H[i - 1] == 3 and H[i] == 1:
                answer += 1
                for i in range(4):
                    H.pop(i - 3)
   
    return answer
   
A = solution([2,1,1,2,3,1,2,3,1])
B = solution([1,3,2,1,2,1,3,1,2])
print(A,B)