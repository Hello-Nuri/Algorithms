def solution(age):
    answer = ''
    alpa = ['a','b','c','d','e','f','g','h','i','j']
    age = str(age)
    
    for c in age:
        answer+= alpa[int(c)]
    return answer
    