def solution(my_strings, parts):
    result_list = []
    for string, (s,e) in zip(my_strings,parts):
        part = string[s:e+1]
        result_list+=part
    return ''.join(result_list)
    