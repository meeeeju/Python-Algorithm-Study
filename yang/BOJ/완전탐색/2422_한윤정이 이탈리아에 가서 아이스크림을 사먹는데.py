# 31932KB / 332ms
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
impossible_set = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    impossible_set[a].add(b)
    impossible_set[b].add(a)

ans = 0
for first_pick in range(1, N+1):
    for second_pick in range(first_pick+1, N+1):
        if second_pick in impossible_set[first_pick]: continue
        for third_pick in range(second_pick+1, N+1):
            if third_pick in impossible_set[first_pick]: continue
            if third_pick in impossible_set[second_pick]: continue
            ans += 1
print(ans)