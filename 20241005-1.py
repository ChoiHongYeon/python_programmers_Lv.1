# 폰켓몬 (https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3)

def solution(nums):

    nums_len = len(nums)
    set_nums = set(nums)
    list_nums = list(set_nums)

    if len(list_nums) >= nums_len / 2:
        return int(nums_len / 2)
    else:
        return len(list_nums)

print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))