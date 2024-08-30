def solution(l, r):
    answer = []
    for i in range(l,r+1):
        str_i = str(i)
        if all(char in '05' for char in str_i):
            answer.append(i)
    if not answer:
        answer = [-1]
    return answer
        