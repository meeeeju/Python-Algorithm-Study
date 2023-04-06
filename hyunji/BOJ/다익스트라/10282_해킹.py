#블로그참고 ㅠㅠ..
import sys
import heapq
input=sys.stdin.readline

T=int(input())

for _ in range(T): #입력받은 T만큼 반복문
    n,d,c=map(int,input().split())
    arr=[[] for _ in range(n+1)] #컴퓨터 의존성 배열 n+1 만큼 할당
    time=[sys.maxsize]*(n+1) #몇초후에 컴퓨터가 감염되는지 확인하는 배열
    time[c]=0
    queue=[[0,c]]
    for _ in range(d): #입력받은 d만큼 반복문
        a,b,s=map(int,input().split())
        arr[b].append([a,s])
    while queue:
        w,s=heapq.heappop(queue)
        for i,j in arr[s]:
            if time[i]>w+j: #저장되어있는 감염시간과 이전꺼에서 뻗어나가는 감염시간 중 작은것을 저장
                time[i]=w+j
                heapq.heappush(queue,[w+j,i])
    maxx=0
    count=0

    for i in time: #time 배열을 돌면서 sys.maxsize가 아닌 max값과 갯수를 구함
        if i!=sys.maxsize: 
            maxx=max(i,maxx)
            count+=1
    print(count,maxx)
