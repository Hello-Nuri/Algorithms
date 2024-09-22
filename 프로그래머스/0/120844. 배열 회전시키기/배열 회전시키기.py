def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        for i in range(len(numbers)-1):
            answer.append(numbers[i])
        
    else:
        answer = numbers[1:]
        answer.append(numbers[0])
    return answer