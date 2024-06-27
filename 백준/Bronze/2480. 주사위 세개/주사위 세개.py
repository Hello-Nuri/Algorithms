dice = list(map(int,input().split()))


for i in range(3):
    if dice[0] == dice[1] == dice[2]:
        answer = 10000+(dice[0])*1000
        print(answer)
        break

    if (dice[0] == dice[1]) or (dice[0] == dice[2]):
        answer = 1000+(dice[0])*100
        print(answer)
        break

    if (dice[1] == dice[2]):
        answer = 1000+(dice[1])*100
        print(answer)
        break
     
    if dice[0] != dice[1] != dice[2]:
        answer = max(dice) * 100
        print(answer)
        break