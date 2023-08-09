# 33300KB / 404ms
import sys
input = sys.stdin.readline

#     0   1   2  3  4  5  6  7
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fb_list = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fb_list.append((r, c, m, s, d))

for _ in range(K):
    # 파이어볼 이동
    fb_move = dict()
    for r, c, m, s, d in fb_list:
        next_r = (r + dr[d]*s)%N
        next_c = (c + dc[d]*s)%N
        if (next_r, next_c) not in fb_move:
            fb_move[(next_r, next_c)] = []
        fb_move[(next_r, next_c)].append((m, s, d))
    # 2개 이상의 파이어볼 있는 칸 합침.
    fb_list = []
    for position, fireball in fb_move.items():
        if len(fireball) == 1:
            fb_list.append((position[0], position[1], fireball[0][0], fireball[0][1], fireball[0][2]))
        else:
            new_m = 0
            new_s = 0
            remainder = fireball[0][2]%2
            is_same = True
            for f in fireball:
                new_m += f[0]
                new_s += f[1]
                if remainder != f[2]%2:
                    is_same = False
            new_m //= 5
            if new_m == 0 :
                continue
            new_s //= len(fireball)
            start = 0 if is_same else 1
            for d in range(start, start+7, 2):
                fb_list.append((position[0], position[1], new_m, new_s, d))
# 정답출력
ans = 0
for r, c, m, s, d in fb_list:
    ans += m
print(ans)