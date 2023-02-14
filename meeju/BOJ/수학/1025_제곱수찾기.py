# 블로그 참고 / 질문 게시판 참고
import sys
import math
input = sys.stdin.readline

# 2 3
# 123
# 456

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

res = -1
for i in range(N):  # i: 시작 행 위치
    for j in range(M):  # j: 시작 열 위치
        for a in range(-N, N):  # a: 행 방향 등차
            for b in range(-M, M):  # b: 열 방향 등차
                num = ''
                y, x = i, j
                # 행과 열 시작 위치부터 등차를 더해가며 숫자 생성
                while 0 <= y < N and 0 <= x < M:
                    num += arr[y][x]
                    if a == 0 and b == 0:
                        break
                    if int(math.sqrt(int(num))) ** 2 == int(num):
                        res = max(int(num), res)
                    y += a
                    x += b
print(res)


