# 40572kb / 720ms
import sys
input = sys.stdin.readline

'''
5 3
1
2
8
4
9'''

N, C = map(int,input().split())  # N : 집의 갯수, C : 공유기의 갯수

dis_home = [0 for _ in range(N)]
for i in range(N):
    dis_home[i] = int(input())
dis_home.sort()

start = 1    # 두 공유기 사이의 거리 중 가장 최소가 될 때
end  = dis_home[-1]-dis_home[0]     # 두 공유기 사이의 거리 중 가장 최대가 될 때 

adj_dis = [ 0 for _ in range(N-1)]
for i in range(N-1): 
    adj_dis[i]= dis_home[i+1]-dis_home[i]

# exist_dis = set()
# for i in range(N-1):
#     for j in range(i,N):
#         exist_dis.add(dis_home[j]- dis_home[i])

while (start <= end):
    mid = (start+end)//2
    count = 1
    prefix_sum = 0 
    for i in range(N-1):
        prefix_sum += adj_dis[i]
        if prefix_sum >= mid :
            prefix_sum = 0
            count +=1
    if count >= C :
        start = mid+1
    elif count < C :
        end = mid-1
print(end)