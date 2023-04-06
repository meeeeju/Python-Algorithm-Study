# 31256KB / 44ms
import sys
input = sys.stdin.readline
N, D = map(int, input().split())
shortcut = []
for _ in range(N):
    a, b, c = map(int, input().split())
    if b > D:
        continue
    shortcut.append((a, b, c))
shortcut.sort(key=lambda x:x[1]) # 도착위치가 가까운 곳 기준으로 정렬
road = [i for i in range(D+1)]
for s, e, d in shortcut:
    if road[e] > road[s]+d:
        for i in range(e+1, D+1):
            road[i] = road[i]-road[e]+road[s]+d
        road[e] = road[s]+d
print(road[D])