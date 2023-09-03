#31256KB/	68ms
'''
1. 금메달 수가 더 많은 나라 
2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라 
'''
import sys

N,K = map(int,sys.stdin.readline().split()) # N: 국가의 수 , K : 등수를 알고 싶은 국가
rank = []
for _ in range(N):
    rank.append(list(map(int,sys.stdin.readline().split())))

rank=sorted(rank,key=lambda x: (-x[1],-x[2],-x[3]))  # 금메달,은메달,동메달 순으로 정렬
index=0
for i in range(N):
    if rank[i][0]==K : index=i  # 정렬된 rank에서 k를 찾아서 저장

for i in range(N):
    if rank[index][1:]==rank[i][1:] and index>i: # 같은 점수를 가지고 있고, index가 더 작으면 공동 등수 이기때문에 index 줄이기
        index=i
        break
print(index+1)
