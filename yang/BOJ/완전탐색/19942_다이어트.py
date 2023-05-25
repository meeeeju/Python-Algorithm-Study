# 	31256KB / 96ms
import sys
input = sys.stdin.readline

def check(food):
    for i in range(4):
        if food[i]<check_list[i]:
            return False
    return True

def dfs(s):
    if check(food):
        global min_price
        global ans_foods
        if min_price > food[-1]:
            min_price = food[-1]
            ans_foods = [temp.copy()]
        elif min_price == food[-1]:
            ans_foods.append(temp.copy())
        return
    for i in range(s, N):
        if not visited[i]:
            visited[i] = True
            temp.append(i+1)
            for j in range(5):
                food[j] += foods[i][j]
            dfs(i+1)
            for j in range(5):
                food[j] -= foods[i][j]
            visited[i] = False
            temp.pop()
            # temp.remove(i+1)
    pass

N = int(input())
foods = []
check_list = list(map(int, input().split())) # 최소 영양성분
for _ in range(N):
    foods.append(list(map(int, input().split())))
visited = [False]*N
ans_foods = []
temp = []
food = [0, 0, 0, 0, 0]
min_price = 500*15+1
dfs(0)
ans_foods.sort()
# print(ans_foods)
if len(ans_foods) == 0:
    print("-1")
else:
    print(min_price)
    print(*(ans_foods[0]))
