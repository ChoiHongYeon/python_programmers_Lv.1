# [PCCP 기출문제] 1번 / 동영상 재생기 (https://school.programmers.co.kr/learn/courses/30/lessons/340213?language=python3)

def solution(video_len, pos, op_start, op_end, commands):

    v = int(video_len[:2]) * 60 + int(video_len[3:])
    p = int(pos[:2]) * 60 + int(pos[3:])
    os = int(op_start[:2]) * 60 + int(op_start[3:])
    oe = int(op_end[:2]) * 60 + int(op_end[3:])

    for i in commands:
        if p >= os and p <= oe:
            p = oe
        if i == "next":
            p = min(p + 10, v)
        else:
            p = max(p - 10, 0)

    if p >= os and p <= oe:
            p = oe

    answer = ""

    if p / 60 < 10:
         answer += "0" + str(int(p / 60))
    else:
         answer += str(int(p / 60))

    answer += ":"

    if p % 60 < 10:
         answer += "0" + str(p % 60)
    else:
         answer += str(p % 60)

    return answer

print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))