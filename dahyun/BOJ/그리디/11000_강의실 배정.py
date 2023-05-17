# 75148 KB / 408 ms
import sys
import heapq
input = sys.stdin.readline
lecture=[0]  # 강의실 - 마치는 시간 저장  (무조건 하나의 강의실은 존재하므로, 0으로 초기화)
N=int(input()) # N : 강의 개수
nlist=[list(map(int,input().split())) for _ in range(N)]  # 모든 S ~ T
for s,t in sorted(nlist):  # 강의 시작 순으로 정렬 
    m = heapq.heappop(lecture)  # m = 강의 종료 시간이 가장 작은 값
    if m>s: heapq.heappush(lecture,m)  # 만약 이번 강의 시작 시간이 m보다 크다면 m 다시 저장
    heapq.heappush(lecture,t) # 현재 마치는 시간 추가 
print(len(lecture))  # 강의실 개수 출력

'''
[첫번째 방법]
lecture=[]
for _ in range(int(input())):
    s,t = map(int,input().split())
    for i in range(len(lecture)):
        if lecture[i]<=s : lecture[i]=t;break
    else: lecture.append(t)
print(len(lecture))
'''

'''
8
1 8
9 16
3 7
8 10
10 14
5 6
6 11
11 12
-> 3

4
1 2
2 2
2 3
3 3
->1

4
2 2
2 2
2 2
2 2
->1
'''
