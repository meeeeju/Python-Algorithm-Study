#블로그 코드
n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])
'''
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
liist=[]
maxx=0
maxx1=0
for _ in range(n):
    w,v=map(int,input().split())
    liist.append([w,v])

n_limit=0
for i in range(n):
    n_limit=liist[i][0]
    if n_limit>k:
        continue
    else:
        maxx1=liist[i][1]
        for j in range(i+1,n):
            n_limit+=liist[j][0]
            if n_limit<=k:
                maxx=max(maxx,maxx1+liist[j][1])
            else:
                continue
print(maxx)'''
