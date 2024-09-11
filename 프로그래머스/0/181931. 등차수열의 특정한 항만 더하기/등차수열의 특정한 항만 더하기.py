def solution(a, d, included):
    answer = 0
    ad_list = [a]
    for i in range(len(included)-1):
        a += d
        ad_list.append(a)
    for index,value in enumerate(included):
        if value:
            answer += ad_list[index]
    return answer