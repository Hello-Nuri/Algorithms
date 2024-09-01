def solution(num_list):
    answer = 0
    even = 0
    odd = 0
    for i,value in enumerate(num_list):
        if (i+1) % 2 == 0:
            even += value
        if (i+1) % 2 != 0:
            odd += value
        
    return max(even,odd)