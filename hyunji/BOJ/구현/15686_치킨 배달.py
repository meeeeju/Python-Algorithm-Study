#메모리 :31256 시간 :788
from itertools import combinations
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
jido=[]
count2=0
chicken=[]
house=[]
for _ in range(n):
    jido.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if jido[i][j]==2:
            count2+=1
            chicken.append([i,j])
        elif jido[i][j]==1:
            house.append([i,j])
result=0
liist=[]
if count2==m:
    for i in range(n):
        for j in range(n):
            if jido[i][j]==1:
                minn=1e8
                for k in range(len(chicken)):
                    minn=min(minn,abs(i-chicken[k][0])+abs(j-chicken[k][1]))
                result+=minn
    print(result)
else:
    chickencombi=list(combinations(chicken,m))

    for k1 in range(len(chickencombi)):
        for i in range(len(house)):
            minn=1e8
            for k2 in range(m):
                minn=min(minn,abs(house[i][0]-chickencombi[k1][k2][0])+abs(house[i][1]-chickencombi[k1][k2][1]))
            result+=minn
        liist.append(result)
        result=0

    print(min(liist))
