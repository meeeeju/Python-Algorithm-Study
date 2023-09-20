# 47740KB / 832ms
# 상하좌우 조건 만족시키는 방법 모르겠어서 블로그 참고
# https://it-and-life.tistory.com/46
from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = []
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))
    mem = [[0]*n for _ in range(2)]
    mem[0][0] = sticker[0][0]
    mem[1][0] = sticker[1][0]
    if n == 1:
        print(max(mem[0][0], mem[1][0]))
        continue
    mem[0][1] = mem[1][0] + sticker[0][1]
    mem[1][1] = mem[0][0] + sticker[1][1]
    for i in range(2, n):
        mem[0][i] += max(mem[1][i-1], mem[1][i-2]) + sticker[0][i]
        mem[1][i] += max(mem[0][i-1], mem[0][i-2]) + sticker[1][i]
    print(max(mem[0][n-1], mem[1][n-1]))



'''
def dp(i):
    if mem[i] != -1:
        return mem[i]
    mem[i] = sticker[i]
    for k in range(i+1, n*2):
        if i + 1 != k and i - 1 != k and i + n != k and i - n != k:
            mem[i] = max(mem[i], sticker[i]+dp(k))
    return mem[i]

T = int(input())
sticker = []
for _ in range(T):
    n = int(input())
    sticker += list(map(int, input().split()))
    sticker += list(map(int, input().split()))
    mem = [-1]*(n*2)
    for i in range(n*2):
        dp(i)
    print(mem)
    print(max(mem))
'''