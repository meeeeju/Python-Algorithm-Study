# 31256KB / 248ms
from sys import stdin
input = stdin.readline

def simulation(archer1, archer2, archer3):
    archer1_sorted_enemy = list(sorted(enemy_list, key=lambda x:(abs(x[0]-N)+abs(x[1]-archer1), x[1]), reverse=True))
    archer2_sorted_enemy = list(sorted(enemy_list, key=lambda x:(abs(x[0]-N)+abs(x[1]-archer2), x[1]), reverse=True))
    archer3_sorted_enemy = list(sorted(enemy_list, key=lambda x:(abs(x[0]-N)+abs(x[1]-archer3), x[1]), reverse=True))
    remove_enemy = set()
    for time in range(N): # time : 적이 아래로 한칸 이동
        # 궁수에게 가장 가깝고, 거리가 D 이하인 적 찾기
        archer1_enemy = -1
        archer2_enemy = -1
        archer3_enemy = -1
        for i in range(len(archer1_sorted_enemy)-1, -1, -1):
            temp_enemy = archer1_sorted_enemy[i]
            if N-temp_enemy[0]-1 < time:
                archer1_sorted_enemy.pop(i)
            else:
                if temp_enemy not in remove_enemy and abs(temp_enemy[0]-N+time)+abs(temp_enemy[1]-archer1) <= D:
                    archer1_enemy = temp_enemy
                    break
        for i in range(len(archer2_sorted_enemy)-1, -1, -1):
            temp_enemy = archer2_sorted_enemy[i]
            if N-temp_enemy[0]-1 < time:
                archer2_sorted_enemy.pop(i)
            else:
                if temp_enemy not in remove_enemy and abs(temp_enemy[0]-N+time)+abs(temp_enemy[1]-archer2) <= D:
                    archer2_enemy = temp_enemy
                    break
        for i in range(len(archer3_sorted_enemy)-1, -1, -1):
            temp_enemy = archer3_sorted_enemy[i]
            if N-temp_enemy[0]-1 < time:
                archer3_sorted_enemy.pop(i)
            else:
                if temp_enemy not in remove_enemy and abs(temp_enemy[0]-N+time)+abs(temp_enemy[1]-archer3) <= D:
                    archer3_enemy = temp_enemy
                    break
        # 궁수 세명이 동시에 공격
        remove_enemy.add(archer1_enemy)
        remove_enemy.add(archer2_enemy)
        remove_enemy.add(archer3_enemy)
    if -1 in remove_enemy:
        remove_enemy.remove(-1)
    return len(remove_enemy)
# 초기화
N, M, D = map(int, input().split()) # 행, 열, 궁수 공격거리
enemy_list = [] # 전체맵
for r in range(N):
    map_list = list(map(int, input().split()))
    for c in range(M):
        if map_list[c] == 1:
            enemy_list.append((r, c))

ans = 0
# 궁수 조합
for archer1 in range(M-2):
    for archer2 in range(archer1+1, M-1):
        for archer3 in range(archer2+1, M):
            # 시뮬레이션
            ans = max(ans, simulation(archer1, archer2, archer3))

# 결과 출력
print(ans)