def solution(my_string, target):
    answer = 0
    for i in range(len(my_string)):
        for j in range(i,len(my_string)):
            if my_string[i:j+1] == target:
                answer = 1
                break
    return answer