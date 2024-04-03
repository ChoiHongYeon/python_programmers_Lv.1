# 둘만의 암호(https://school.programmers.co.kr/learn/courses/30/lessons/155652)

def solution(s, skip, index):
    skip_num=sorted([ord(i) for i in skip])
    for j in range(len(skip)):
        skip_num.append(skip_num[j]+26)
    for k in range(len(skip)):
        skip_num.append(skip_num[k]+52)

    s_num=[ord(i) for i in s]

    for a in range(len(s)):
        for b in range(index):
            l=True
            while l==True:
                if s_num[a]+1 not in skip_num:
                    s_num[a]+=1
                    l=False
                else:
                    s_num[a]+=1

    for c in range(len(s)):
        while s_num[c]>122:
            s_num[c]-=26

    answer=''.join(chr(d) for d in s_num)

    return answer