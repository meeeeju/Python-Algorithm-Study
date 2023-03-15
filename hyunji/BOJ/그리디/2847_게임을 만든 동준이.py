#메모리 :31256 시간 :40ms
import sys
input=sys.stdin.readline
N=int(input())
liist=[]
count=0
for i in range(N):
    score=int(input())
    liist.append(score)


for i in range(N-1,0,-1):
    if liist[i-1]>=liist[i]:
        count+=liist[i-1]-(liist[i]-1)
        liist[i-1]=liist[i]-1
print(count)
