def solution(n, slicer, num_list):
    answer = []
    a, b, c = slicer
    if n == 1:
        return num_list[0:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3 :
        return num_list[a:b+1]
    elif n == 4 :
        for i,value in enumerate(num_list[a:b+1]):
            if i % c == 0:
                answer.append(value)
        return answer