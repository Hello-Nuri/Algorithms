def solution(arr, n):
    result = []
    if len(arr) % 2 == 0:
        for i in range(len(arr)):
            if i % 2 != 0:
                result.append(arr[i]+n)
            else:
                result.append(arr[i])
    else:
        for i in range(len(arr)):
            if i % 2 == 0:
                result.append(arr[i]+n)
            else:
                result.append(arr[i])
    return result