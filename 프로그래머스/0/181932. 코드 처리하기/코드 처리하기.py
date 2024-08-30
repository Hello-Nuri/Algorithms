def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        if mode == 0 and code[idx] != '1' and idx % 2 == 0:
            answer+=code[idx]
        if mode == 0 and code[idx] == '1':
            mode = 1
            continue
        if mode == 1 and code[idx] != '1' and idx % 2 != 0:
            answer += code[idx]
        if mode == 1 and code[idx] == '1':
            mode = 0
            continue
    if answer == '':
        return "EMPTY"            
    return answer