def solution(my_string, alp):
    answer = ''
    for c in my_string:
        if alp in c:
            answer += c.upper()
        if alp not in c:
            answer += c
    return answer