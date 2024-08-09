def solution(num, n):
    if num % n == 0:
        return 1
    if num % n != 0:
        return 0