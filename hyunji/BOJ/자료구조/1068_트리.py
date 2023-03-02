#블로그 참고
#메모리 :31256 시간 :44ms
import sys
input=sys.stdin.readline

N=int(input())
parent=list(map(int,input().split()))
remove_parent=int(input())

tree=[[] for i in range(N+1)]
liist=[]
count=0

def check(n):
    global count
    if tree[n]:
        for i in tree[n]:
            check(i)
    else:
        count+=1
        
for i in range(N):
    if parent[i]==-1:
        liist.append(i)
        
    if parent[i]!=-1 and i!=remove_parent:
        tree[parent[i]].append(i)
        
for i in liist:
    if i!=remove_parent:
        check(i)
print(count)
