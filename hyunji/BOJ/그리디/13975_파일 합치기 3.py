#블로그참고
import heapq
t=int(input())
for _ in range(t):
    k=int(input())
    liist=list(map(int,input().split()))
    liist.sort()
    queue=[]
    summ=0
    for i in liist:
        heapq.heappush(queue,i)
    while len(queue)>1:
        a=heapq.heappop(queue)
        b=heapq.heappop(queue)
        heapq.heappush(queue,a+b)
        summ+=a+b
    print(summ)
    
    
