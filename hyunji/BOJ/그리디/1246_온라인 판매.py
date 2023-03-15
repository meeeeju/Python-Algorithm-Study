#메모리 :31256 시간: 56ms
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
liist=[]
liist2=[]

count=0
price=0
income=0

for i in range(M):
    P=int(input())
    liist.append(P)
liist.sort()
if N<M:
    liist.reverse()
    for i in range(N):
        count=i+1
        liist2.append((liist[i],count*liist[i]))
        price,income=max(liist2,key=lambda x:x[1])
    print(price,income)
        
else:
    for i in range(len(liist)):
        count=len(liist)-i
        liist2.append((liist[i],count*liist[i]))
        price,income=max(liist2,key=lambda x:x[1])
    print(price,income)
