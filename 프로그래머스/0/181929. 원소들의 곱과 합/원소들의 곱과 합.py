def solution(num_list):
    sum_num = sum(num_list)**2
    times_num = 1
    for i in range(len(num_list)):
         times_num *= num_list[i]
    
    if times_num > sum_num:
        return 0
    else:
        return 1