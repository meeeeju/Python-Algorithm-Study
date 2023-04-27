# 	31256kb / 	48ms
import sys
input = sys.stdin.readline

'''
3
3
0 1 0
1 0 1
0 1 0
1 2 3'''

def root(i):
	while i != ids[i]: i=ids[i]
	return i

def union(p,q):
	id1,id2 = root(p), root(q)
	if id1 == id2 : return
	if size[id1] <= size[id2]:
			ids[id1]=id2
			size[id2]+=size[id1]
	else:
			ids[id2]=id1
			size[id1]+=size[id2]
			


N = int(input()) # 도시의 수
M = int(input()) # 여행 계획에 속한 도시들의 수

city_info =[0 for _ in range(N)]
for i in range(N):
	city_info[i]=list(map(int,input().split()))
tour_list = list(map(int,input().split()))

ids=[]  
size=[] 
for idx in range(N):
	ids.append(idx) # 도시의 번호는 1부터 N 까지 주어지므로
	size.append(1)
			
for i in range(N):
	for j in range(N):
		if city_info[i][j]:
			union(i,j)

root_city = root(tour_list[0]-1)
for city in tour_list:
	if root_city != root(city-1):
		print("NO")
		break
else:
	print("YES")
