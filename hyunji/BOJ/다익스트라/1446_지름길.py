#블로그보고 수정,,,
#메모리 :31256 시간 :44ms
import sys
input=sys.stdin.readline
N,D=map(int,input().split())
liist=[]
liist2=[]
distance=[i for i in range(D+1)]

for i in range(N):
    liist.append(list(map(int,input().split())))
liist.sort(key=lambda x:x[0])

for i in range(N):
    if (liist[i][1]- liist[i][0])>liist[i][2]:
       liist2.append(liist[i])

for i in range(D+1):
    if i>0:
        distance[i]=min(distance[i],distance[i-1]+1)
    for j in range(len(liist2)):
        if liist2[j][1]<=D and liist2[j][0]==i and distance[i]+liist2[j][2]<distance[liist2[j][1]]:
            distance[liist2[j][1]]=distance[i]+liist2[j][2]
print(distance[D])
