# 31256	44
import sys
input = sys.stdin.readline

# dfs 를 사용하자 !
#  output : 최소 몇 개의 칸에 선물
# topological sort 로 cycle 탐지하는 방법

'''
input 
6
EEWWEW'''

N = int(input())    
direction_info = input().rstrip()   # 지도 정보 (E : +1 , W : -1)
graph = [ [] for _ in range(N)]  # 번호를 0 ~ N-1 까지 부여

def root(i):
	while i != ids[i]: i=ids[i]
	return i

def connected(p,q):
	return root(p)==root(q)

def union(p,q):
	id1,id2 = root(p), root(q)
	if id1 == id2 : return
	if size[id1] <= size[id2]:
			ids[id1]=id2
			size[id2]+=size[id1]
	else:
			ids[id2]=id1
			size[id1]+=size[id2]


ids=[]
size=[]
for idx in range(N):
	ids.append(idx)
	size.append(1)

for i in range(N):
    if  direction_info[i] =='E':
        union(i,i+1)
        pass
    else:
        union(i,i-1)
        graph[i].append(i-1)

print(len(set(ids)))





