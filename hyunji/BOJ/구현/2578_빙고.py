# 블로그 참고
# 메모리 :31256 시간 :44
import sys

input = sys.stdin.readline

player = []
mc = []
count = 0

for i in range(5):
    player.append(list(map(int, input().split())))

for i in range(5):
    mc += list(map(int, input().split()))


def check():
    bingo = 0

    for i in range(5):
        if player[i].count(0) == 5:
            bingo += 1

    for i in range(5):
        flag0 = 0
        for j in range(5):
            if player[j][i] == 0:
                flag0 += 1
        if flag0 == 5:
            bingo += 1

    flag1 = 0
    for i in range(5):
        if player[i][i] == 0:
            flag1 += 1
    if flag1 == 5:
        bingo += 1

    flag2 = 0
    for i in range(5):
        if player[i][4 - i] == 0:
            flag2 += 1
    if flag2 == 5:
        bingo += 1

    return bingo


for i in range(25):
    for x in range(5):
        for y in range(5):
            if mc[i] == player[x][y]:
                player[x][y] = 0
                count += 1
    if count >= 12:
        result = check()

        if result >= 3:
            print(i + 1)
            break
