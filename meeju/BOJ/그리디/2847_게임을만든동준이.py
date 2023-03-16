#31256kb	/ 40ms
import sys
input = sys.stdin.readline


N = int(input()) # 레벨의 수
level_score = [0 for _ in range(N)]
visited =[False for _ in range(N)]
for i in range(N):
    level_score[i]=int(input())

cnt = 0
for i in range(N-1,0,-1):
    if level_score[i] <= level_score[i-1]:
        cnt += level_score[i-1]-level_score[i]+1
        level_score[i-1]=level_score[i]-1
        

print(cnt)

            
            