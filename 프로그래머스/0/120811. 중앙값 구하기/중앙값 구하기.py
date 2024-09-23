def solution(array):
    answer = 0
    for i,value in enumerate(sorted(array)):
        if len(array) // 2 == i:
            answer += value
    return answer
        