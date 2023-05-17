# 51012KB / 456ms
# https://www.acmicpc.net/board/view/86573
# 질문게시판 반례 참고.. 이거없었으면 못풀었을듯 ㅠㅠ

import sys
input = sys.stdin.readline

N = int(input())
flowers = []

#  4, 6, 9, 11월은 30일까지 있고, 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며, 2월은 28일까지만 있다.)
changes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(N):
    startM, startD, endM, endD = map(int, input().split())
    start = 0
    for i in range(1, startM):
        start += changes[i]
    start += startD
    end = 0
    for i in range(1, endM):
        end += changes[i]
    end += endD
    flowers.append((start, end))

december = 0
for i in range(11):
    december += changes[i]
december += 30

answer = 0
last = changes[1]+changes[2]+1 # 3월 1일. 보기 시작하는 기준점.
maxTemp = last
flowers.sort(key=lambda x:(x[0],-x[1])) # 시작일 오름차순 / 끝나는날 내림차순

i = 0
while i<len(flowers):
    start, end = flowers[i][0], flowers[i][1]

    if start <= last < end: # 현재 보는 일 사이에 있음.
        maxTemp = max(maxTemp, end)
        if i == len(flowers)-1: # 맨 마지막일때 maxTemp 하나 고름.
            answer += 1

    elif start > last: # 기준점 이동
        answer += 1 # 범위 밖에 벗어났을 때 maxTemp 하나 고름
        last = maxTemp # 기준점 maxTemp로 이동
        if maxTemp > december: # 이미 12월이면 종료
            break
        if last < start: # 안이어지는 경우 -> 연속적으로 못고름
            answer = 0
            break
        i -= 1 # 바뀐 기준점으로 한번 더 보기
    i += 1

if maxTemp <= december:
    answer = 0
print(answer)
