def solution(rny_string):
    answer = ''
    for c in rny_string:
        if 'm' not in c:
            answer += c
        if 'm' in c:
            answer += 'rn'
    return answer