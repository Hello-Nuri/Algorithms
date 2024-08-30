def solution(n, k):
    answer = []
    for i in range(1,n+1):
        if k * i in range(1,n+1):
            answer.append(i*k)
    return answer