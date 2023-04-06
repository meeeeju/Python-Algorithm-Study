#baekJoon 13913 숨바꼭질 4
import heapq
def dijstra(start):
    heap=[(0,start)]  # 시간, 현재 위치
    distance[start]=0  # 시작 위치는 0으로 초기화
    while heap:
        time,cur=heapq.heappop(heap)  
        if cur==K: return time  # 만약 현재위치가 K면 time 리턴
        if 0<=cur+1<=100000 and distance[cur+1]>distance[cur]:  # 해당 계산 값이 범위 안에 있고, 최단거리일 경우
            distance[cur+1]=distance[cur]  
            parent[cur+1]=cur  # 부모 저장
            heapq.heappush(heap,(time+1,cur+1))
        if 0<=cur-1<=100000 and distance[cur-1]>distance[cur]:
            distance[cur-1]=distance[cur]
            parent[cur-1]=cur
            heapq.heappush(heap,(time+1,cur-1)) 
        if 0<=cur*2<=100000 and distance[cur*2]>distance[cur]:
            distance[cur*2]=distance[cur]
            parent[cur*2]=cur
            heapq.heappush(heap,(time+1,cur*2)) 
        
        

N,K = map(int,input().split()) # N : 시작 위치 , K : 도착 위치
distance=[100000000000 for _ in range(100002)]  # 최단 거리 배열
parent=[i for i in range(100002)]   # 부모 저장 배열
result=[]
time=dijstra(N)
print(time)

while parent[K]!=K: # K위치에서부터 부모노드로 거슬러 올라감
    result.append(K)
    K=parent[K]
result.append(N)
print(*(reversed(result)))  #뒤집에서 출력  
