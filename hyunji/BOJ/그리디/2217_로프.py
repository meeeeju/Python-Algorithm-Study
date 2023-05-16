#메모리 :35500 시간 :136
import sys
input=sys.stdin.readline

n=int(input())
liist=[]

for i in range(n):
    rope=int(input())
    liist.append(rope)
liist.sort()
maxx=0
for i in range(n):
    maxx=max(maxx,liist[i]*(n-i))

print(maxx)
