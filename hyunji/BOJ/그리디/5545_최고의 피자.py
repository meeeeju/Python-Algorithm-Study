#메모리 :31256 시간:40ms
import sys
input=sys.stdin.readline

N=int(input())
A,B=map(int,input().split())
C=int(input())
D=[]
liist=[]
liist2=[]
dow=0
for i in range(N):
    D.append(int(input()))

D.sort()
D.reverse()
for i in range(N):
    dow+=D[i]
    liist.append(dow)

for i in range(N):
    price=A+B*(i+1)
    liist2.append((C+liist[i])//price)
liist2.append(C//A)
print(max(liist2))
