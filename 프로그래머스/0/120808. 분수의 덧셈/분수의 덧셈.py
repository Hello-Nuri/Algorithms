def solution(numer1, denom1, numer2, denom2):
    answer = []
    answer = [(numer1*denom2)+(numer2*denom1), denom1*denom2]

    gdc = GCD(answer[0], answer[1])

    return [answer[0]/gdc, answer[1]/gdc]

def GCD(a, b):
    while(b>0):
        a, b = b, a%b
    return a