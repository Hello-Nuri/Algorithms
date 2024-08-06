def solution(my_string, overwrite_string, s):
    start = my_string[:s]
    end = my_string[s + len(overwrite_string):]
    return start + overwrite_string + end