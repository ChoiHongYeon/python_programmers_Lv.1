# 행렬의 덧셈 (https://school.programmers.co.kr/learn/courses/30/lessons/12950)

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j] + arr2[i][j])

    return answer

return1 = solution([[1,2],[2,3]], [[3,4],[5,6]])
return2 = solution([[1],[2]], [[3],[4]])

print(return1)
print(return2)