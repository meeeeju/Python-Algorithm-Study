# 38984KB / 288ms
# 블로그 참조
# https://mgyo.tistory.com/374

import sys
input = sys.stdin.readline

def check(limit, N, C, homes):
    install = homes[0]
    count = 1
    for i in range(1, N):
        if homes[i]-install >= limit:
            install = homes[i]
            count += 1
    if count >= C: return True # 공유기를 더 설치할 수 있음
    return False

def solve2110(N, C, homes):
    start = 1
    end = homes[N-1]-homes[0]+1
    while start+1<end:
        mid = (start+end)//2
        if check(mid, N, C, homes):
            start = mid
        else: end = mid
    return start

N, C = map(int, input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))
homes.sort()

print(solve2110(N, C, homes))

'''import sys
from itertools import combinations
input = sys.stdin.readline

N, C = map(int, input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))
homes.sort()
combi = combinations(homes, C)
ans = 0
for c in combi:
    distance = homes[N-1]-homes[0]
    for i in range(1, len(c)):
        distance = min(distance, c[i]-c[i-1])
    ans = max(distance, ans)
print(ans)'''
