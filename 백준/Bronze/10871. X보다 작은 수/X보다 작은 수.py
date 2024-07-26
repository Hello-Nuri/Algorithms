n, X = map(int,input().split())
listn = list(map(int,input().split()))


for i in range(n):
    if listn[i] < X:
         print(listn[i], end = ' ')