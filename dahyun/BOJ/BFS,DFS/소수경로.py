# 36324 KB / 160 ms
import sys
import math
from collections import deque
def decimal(number): # 에라토스테네스의 체
    graph=[True for _ in range(number+1)]
    graph[0]=False
    graph[1]=False
    for i in range(2, int(math.sqrt(number))+1):
        if graph[i]:
            j=1
            while j*i<=number:
                graph[j*i]=False
                j+=1
    return graph
            
def bfs(A,B,graph):
    count=100000
    queue=deque()
    queue.append((A,0))
    visited=[False for _ in range(10001)]
    visited[int(A)]=True
    while len(queue)!=0:
        a,c = queue.popleft()
        if c>count : continue 
        if a==B :  
            count=c
            continue
        for i in range(4):  # 네자리 수 인덱스 하나씩
            if a[i]==B[i]: continue
            for j in range(0,10): # 각 자리수마다 0~9까지의 수 넣어본다
                if i==0 and j==0: continue # 첫번째 자리수가 0이면 4자리 자연수가 되지 않으므로 pass
                num=int(a[:i]+str(j)+a[i+1:])
                if j!=int(a[i]) and graph[num] and visited[num]==False: # 소수가 맞는지 , 방문한 적이 있는지 확인
                    visited[num]=True
                    queue.append((str(num),c+1))
    return count

def main():             
    graph=decimal(10000)       
    for _ in range(int(sys.stdin.readline())):
        A,B = map(int,sys.stdin.readline().split())
        count=bfs(str(A),str(B),graph)
        if count==100000 : print("Impossible")
        else : print(count)
        
main()
