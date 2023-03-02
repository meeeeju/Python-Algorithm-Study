#블로그참조
#메모리 :76720 시간 :312ms
import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

n,m=map(int,input().split())

liist=[i for i in range(n+1)]

def find(x):
    if liist[x]!=x:
        liist[x]=find(liist[x])
    return liist[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        liist[b]=a
    else:
        liist[a]=b
        
for _ in range(m):
    check,a,b=map(int,input().split())
    if check==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
