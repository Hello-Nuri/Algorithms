n = int(input())
a = map(int,list(input().split()))
v = int(input())

cnt = 0
for i in range(n):
    if v in a:
        cnt += 1
print(cnt)