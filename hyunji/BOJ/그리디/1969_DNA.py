#메모리 :31256 시간 :64
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
liist=[]
liist2=[]
answer=[]
count=0

for _ in range(n):
    a=list(input())
    liist.append(a)

for i in range(m):
    acount,tcount,gcount,ccount=0,0,0,0
    for j in range(n):
        if liist[j][i]=='A':
            acount+=1
        elif liist[j][i]=='T':
            tcount+=1
        elif liist[j][i]=='G':
            gcount+=1
        elif liist[j][i]=='C':
            ccount+=1
    
    liist2=[('A',acount),('T',tcount),('G',gcount),('C',ccount)]
    liist2.sort(key=lambda x:(-x[1],ord(x[0])))
    answer.append(liist2[0][0])
    liist2.clear()
for i in range(n):
    for j in range(m):
        if liist[i][j]!=answer[j]:
            count+=1
print("".join(answer))
print(count)

