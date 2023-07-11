#블로그 참고
import heapq
n=int(input())
liist=[]
for _ in range(n):
    deadline,cup=map(int,input().split())
    liist.append((deadline,cup))
liist.sort()

queue=[]
for i in liist:
    heapq.heappush(queue,i[1])
    if i[0]<len(queue):
        heapq.heappop(queue)
print(sum(queue))
