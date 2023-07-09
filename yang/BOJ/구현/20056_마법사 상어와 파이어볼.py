# 33300KB / 912ms
import sys
input = sys.stdin.readline

#     0   1   2  3  4  5  6  7
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

one = []
two = dict()

# N : 격자 크기 / M : 파이어볼 개수 / K : 이동 횟수
N, M, K = map(int, input().split())
for _ in range(M):
    # r : 행 / c : 열
    # m : 질량 / s : 속력 / d : 방향
    r, c, m, s, d = map(int, input().split())
    one.append((r, c, m, s, d))

for _ in range(K):
    # 1번 연산 - 이동
    two = dict()
    for r, c, m, s, d in one:
        newR = r + dr[d]*s
        newC = c + dc[d]*s
        while newR < 1:
            newR += N
        while newR > N:
            newR -= N
        while newC < 1:
            newC += N
        while newC > N:
            newC -= N
        if (newR, newC) not in two:
            two[(newR, newC)] = []
        two[(newR, newC)].append((m, s, d))
    # 2번 연산 - 2개 이상의 파이어볼이 있는 칸
    one = []
    for position, fireball in two.items():
        if len(fireball) == 1:
            one.append((position[0], position[1], fireball[0][0], fireball[0][1], fireball[0][2]))
        else:
            newM = 0
            newS = 0
            remainder = fireball[0][2]%2
            isRemainderSame = True
            for f in fireball:
                newM += f[0]
                newS += f[1]
                if remainder != f[2]%2:
                    isRemainderSame = False
            newM = newM // 5
            if newM == 0 : continue
            newS = newS // len(fireball)
            start = 0 if isRemainderSame else 1
            for d in range(start, start+7, 2):
                one.append((position[0], position[1], newM, newS, d))
# 정답출력
ans = 0
for r, c, m, s, d in one:
    ans += m
print(ans)