def solution(n):
    answer = 0
    if n % 2 != 0:
        for i in range(n):
            if (i+1) <= n and (i+1) % 2 != 0:
                answer +=(i+1)
    if n % 2 == 0:
        for i in range(n):
             if (i+1) <= n and (i+1) % 2 == 0:
                    answer += (i+1)*(i+1)

    return answer