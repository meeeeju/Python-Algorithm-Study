# 218280 KB / 5904 ms (pypy)
import sys
input = sys.stdin.readline
N=int(input())
nlist = list(map(int,input().split()))
need=0 # 화살 개수
while True:
    h=max(nlist)  # 가장 큰 높이
    if h==0: # 가장 큰 높이가 0이면 모두 다 0이므로 종료
        print(need)
        break
    for i in range(N):
        if nlist[i]==h: # nlist[i]가 h랑 같다면 화살로 쏠 수 있음
            h-=1 # 화살로 맞췄으니 높이 1 줄이기
            nlist[i]=0 # 화살로 맞췄으니 해당 위치는 0
    need+=1 # 한바퀴 돌았으니 화살 개수 증가
