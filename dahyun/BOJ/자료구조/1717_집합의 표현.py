# 80524 KB / 348 ms
# 교수니 코드 참고
import sys
input=sys.stdin.readline
def root(i): # 루트 찾는 함수
    while i!= idx[i]: i= idx[i]
    return i
def connected(a,b): # 연결되어 있는 지 확인
    return root(a) == root(b) 
def union(a,b): # 연결시켜주기 : 이때 , 사이즈가 더 작은 것 아래로 붙임
    id1,id2 = root(a),root(b)
    if size[id1]>=size[id2]:
        idx[id2]=id1
        size[id2]+=id1
    else:
        idx[id1]=id2
        size[id1]=id2
    
    
n,m = map(int,input().split())
idx = [i for i in range(n+1)]
size= [1 for _ in range(n+1)]
for _ in range(m):
    fun, a, b = map(int,input().split())
    if fun==0 : union(a,b)
    elif fun==1 : 
        if connected(a,b) : print("YES")
        else : print("NO")
