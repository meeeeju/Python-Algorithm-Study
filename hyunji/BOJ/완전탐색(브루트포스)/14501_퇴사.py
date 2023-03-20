#블로그 참조
#메모리 :31256 시간 :44ms
import sys
input=sys.stdin.readline

N=int(input())

T=[]
P=[]
liist=[0 for i in range(N+1)]

for i in range(N):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)
   
for i in range(N-1,-1,-1):
    if T[i]+i>N:
        liist[i]=liist[i+1]
    else:
        liist[i]=max(liist[i+1],P[i]+liist[T[i]+i])
print(liist[0])
    
