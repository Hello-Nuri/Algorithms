def solution(a, b):
    answer = 0
    A = str(a)+str(b)
    B = str(b)+str(a)
    list = [int(A),int(B)]
    if A == B:
        answer += int(A)
        return answer
    return max(list)