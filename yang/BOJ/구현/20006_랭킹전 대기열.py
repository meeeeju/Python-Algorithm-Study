# 31256KB / 40ms
import sys
input = sys.stdin.readline
p, m = map(int, input().split()) # 플레이어의 수, 방 한개의 정원
room = []
for _ in range(p):
    l, n = input().split()
    l = int(l)
    n = n.strip()
    for r in room:
        if len(r)<m and r[0][0]-10<=l<=r[0][0]+10:
            r.append((l, n))
            break
    else:
        room.append([(l, n)])
for r in room:
    r.sort(key=lambda x: x[1])
    if len(r) == m:
        print("Started!")
    else:
        print("Waiting!")
    for i in r:
        print(*i)