#BaekJoon 1976 여행가자
# 31256 KB / 48 ms
# union 함수 잘못 짜서 자꾸만 시간초과나서 오래걸림 ㅠ
import sys
input=sys.stdin.readline
def root(a):
    while uf[a]!=a: a=uf[a]
    return a

def connect(a,b):
    return root(a)==root(b)

def union(a,b):
    id1, id2 = root(a),root(b)
    if size[id1]>size[id2]:
        uf[id2]=id1
        size[id1]+=size[id2]
    else:
        uf[id1]=id2
        size[id2]+=size[id1]

N=int(input())
M=int(input())
uf=[i for i in range(N)]  # 부모 값 저장
size=[1 for _ in range(N)]  # 달려있는 노드 수
check=set() # union한 노드인지
for i in range(N):
    con = list(map(int,input().split()))
    for j in range(N):
        if con[j]==1: 
            if (i,j) in check or (j,i) in check: continue # 한번 union 해주었던 것은 pass
            union(i,j)
            check.add((i,j)) 

plan = list(map(int,input().split()))
for i in range(1,M):
    if not connect(plan[i-1]-1,plan[i]-1):
        print("NO")
        exit(0)
print("YES")
