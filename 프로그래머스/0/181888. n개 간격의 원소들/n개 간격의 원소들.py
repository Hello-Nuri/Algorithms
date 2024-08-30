def solution(num_list, n):
    answer = []
    for i in range(len(num_list)):
        if i*n < len(num_list):
            answer.append(num_list[i*n])
    return answer