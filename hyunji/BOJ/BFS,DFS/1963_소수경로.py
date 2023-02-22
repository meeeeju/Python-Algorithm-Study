#블로그 참조
#메모리 :36264 #시간 :144ms
import math
from collections import deque

def sosoo():
    for i in range(2, 100):
        if prime[i] == True:
            for j in range(2*i, 10000, i):
                prime[j] = False
def bfs():
    q=deque()
    q.append([a,0])
    
    visit=[0]*10000
    visit[a]=1
    
    while q:
        curr,count=q.popleft()
        strcurr=str(curr)
        
        if curr==b:
            return count
        
        for i in range(4):
            for j in range(10):
                temp=int(strcurr[:i]+str(j)+strcurr[i+1:])
                
                if visit[temp]==0 and prime[temp] and temp>=1000:
                    visit[temp]=1
                    q.append([temp,count+1])


T=int(input())
prime=[True for i in range(10000)]
sosoo()

for i in range(T):
    a,b=map(int,input().split())
    count=bfs()
    
    if count==None:
        print("Impossible")
    else:
        print(count)

