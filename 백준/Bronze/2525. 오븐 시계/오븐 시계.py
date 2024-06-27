a = list(map(int,input().split()))
cook = int(input())
# print(a,type(a))
# print(cook,type(cook))

H = a[0] 
M = a[1]

total_min = (H * 60) + M + cook

h = int(total_min // 60) % 24
m = int(total_min % 60)
print(h,m)