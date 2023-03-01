# 79648KB / 1428ms -> 왜 이렇게 많이걸리지..
import sys
input = sys.stdin.readline


def union(a,b):
    i,j =root(a),root(b)
    if i==j:
        return 
    if sized[i] >= sized[j]:
        arr[j]=i
        sized[i]+=sized[j]
    else:
        arr[i]=j
        sized[j]+=sized[i]
    

def connected(a,b):
    if root(a)==root(b):
        return "YES"
    return "NO"

def root(i):
    while i != arr[i]:
        i = arr[i]
    return i

N ,M= map(int,input().split())    # 집합의 갯수(N) , 연산의 갯수(M)


arr = [i for i in range(N+1)]
sized =[1 for _ in range(N+1)]
anw=''
for _ in range(M):

    operation,a,b = map(int,input().split())

    if operation:   # 1: 같은 집합인지 확인
        anw += connected(a,b)+'\n'
    else:
        union(a,b)
print(anw)


