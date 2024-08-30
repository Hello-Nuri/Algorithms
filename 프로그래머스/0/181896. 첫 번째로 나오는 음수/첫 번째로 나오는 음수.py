def solution(num_list):
    answer = -1
    for i,num in enumerate(num_list):
        if num < 0:
            answer += i+1
            break
    return answer