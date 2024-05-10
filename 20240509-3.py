# 햄버거 만들기(https://school.programmers.co.kr/learn/courses/30/lessons/133502)

def solution(H):
    answer = 0
    i=0
    while i+3 <= len(H):
        if H[i] == 1 and H[i+1] == 2 and H[i+2] == 3 and H[i+3] == 1:
            del H[i:i+4]
            answer += 1
            if i >= 3:
                i -= 3
            else:
                i = 0
        else:
            i += 1
    return answer