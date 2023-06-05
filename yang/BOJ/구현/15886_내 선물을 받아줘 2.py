# 31256KB / 40ms

N = int(input())
road = input()
gift = 0
# cycle의 개수 = 덩어리의 개수 = gift를 줘야하는 개수
for i in range(1, N):
    if road[i-1] == 'E' and road[i]=='W':
        gift += 1
print(gift)