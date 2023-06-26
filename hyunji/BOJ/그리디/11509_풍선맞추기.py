#다현이 코드 참고ㅎㅎ
#메모리 :218280 시간 :5892
import sys
input=sys.stdin.readline
n=int(input())
liist=list(map(int,input().split()))
count=0
while True:
    h=max(liist)
    if h==0:
        print(count)
        break
    for i in range(n):
        if liist[i]==h:
            h-=1
            liist[i]=0
    count+=1
'''
t=0
for i in range(len(liist)):
    
    if liist[i]!=0:
        count+=1
    t=i
    for j in range(1,(len(liist)-i)):
        t+=1
        if liist[t]==liist[i]-j:
            liist[t]=0
    liist[i]=0

print(count)'''
