# 31256 KB /44 ms
import sys
N,newScore,P=map(int,sys.stdin.readline().split()) # N : 전체 점수 수, newScore : 태수의 점수 , P : 랭킹에 드는 수
nlist=list(map(int,sys.stdin.readline().split()))  # nlist : 점수들
count=0
for i in range(N):  
    if newScore>=nlist[i] :   # 태수의 점수가 더 크거나, 같으면 해당 자리에 태수 점수 삽입
        nlist.insert(i,newScore)
        break
    count+=1  # 등수 계속 증가
else: nlist.insert(-1,newScore)  # 태수의 점수가 nlist의 모든 점수보다 작다면 마지막에 추가
if count+nlist.count(newScore)<=P: print(count+1) # 만약 등수 + 태수의 점수의 개수가 랭킹안에 든다면 등수 출력
else: print(-1)
