def solution(my_string, m, c):
    answer = ''
    if c == 1:
        return my_string[::m]
    else:
        return my_string[c-1::m]