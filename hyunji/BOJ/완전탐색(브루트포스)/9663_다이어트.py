# 메모리 :31288 #시간 :196
from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
mp, mf, ms, mv = map(int, input().split())
food = []

maxx = 987654321
result = []
for i in range(n):
    p, f, s, v, c = list(map(int, input().split()))
    food.append([p, f, s, v, c])

for i in range(1, n + 1):
    for summ in combinations(range(1, n + 1), i):
        pp = ff = ss = vv = cc = 0

        for j in summ:
            pp += food[j - 1][0]
            ff += food[j - 1][1]
            ss += food[j - 1][2]
            vv += food[j - 1][3]
            cc += food[j - 1][4]

        if pp >= mp and ff >= mf and ss >= ms and vv >= mv:
            if maxx > cc:
                maxx = cc
                result = summ
            elif maxx == cc:
                result = sorted((result, summ))[0]

if maxx == 987654321:
    print(-1)
else:
    print(maxx)
    print(*result)
