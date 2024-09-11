def solution(myString):
    answer = ''
    low_string = myString.lower()
    for c in low_string:
        if 'a' in c:
            answer+='A'
        if 'a' not in c:
            answer += c
    return answer