#블로그 참고,,,
import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

parent=[i for i in range(N)]

def union(i,j):
    i=find(i)
    j=find(j)
    if i<j:
        parent[j]=i
    else:
        parent[i]=j

def find(N):
    if parent[N]==N:
        return N
    parent[N]=find(parent[N])
    return parent[N]

graph=[]
for i in range(N):
    graph=list(map(int,input().rstrip().split()))
    for j in range(len(graph)):
        if graph[j]==1:
            union(parent[i],parent[j])

liist=list(map(int,input().rstrip().split()))
for i in range(len(liist)):
    liist[i]-=1
temp=find(liist[0])

def answer(liist,temp):
    for i in range(len(liist)):
        if find(liist[i])!=temp:
            return "NO"
    return "YES"
print(answer(liist,temp))
