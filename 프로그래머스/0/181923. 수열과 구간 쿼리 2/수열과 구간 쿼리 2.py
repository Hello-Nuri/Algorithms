def solution(arr, queries):
    answer = []
    
    for s,e,k in queries:
        tem = []
        for i in range(s,e+1):
            if arr[i] > k:
                tem.append(arr[i])
        if tem:
            answer.append(min(tem))
        else:
            answer.append(-1)
    return answer
                