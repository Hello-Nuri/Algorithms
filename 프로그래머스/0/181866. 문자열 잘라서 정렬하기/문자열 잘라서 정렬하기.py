def solution(myString):
    answer = []
    a = myString.split('x')
    for i in a:
        if i != '':
            answer.append(i)
    return sorted(answer)