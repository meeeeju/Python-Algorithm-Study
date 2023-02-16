# 67412KB / 316ms
import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 늘려주기

def dfs(x,visited):  
    visited[x] = True  # x 방문
    for i in g[x]: # i : x와 연결되어 있는 값
        if visited[i] : continue # 만약 i를 방문하였으면 pass
        else :   # 방문하지 않았으면
            graph[i]=x # i의 부모는 x
            dfs(i, visited) # i에 대해서 dfs
    return 

def main():
    global g
    global graph
    N=int(sys.stdin.readline())
    g=[[] for _ in range(N+1)]  # 모든 연결을 나타내는 그래프 (입력받는 수를 대상)
    graph=[0 for _ in range(N+1)] # 부모 노드를 알 수 있는 배열
    visited=[False for _ in range(N+1)] # 방문여부
    
    # 입력받는 데이터를 g에 저장 (모든 연결 저장)
    for _ in range(N-1):
        A,B=map(int,sys.stdin.readline().split())
        g[A].append(B)
        g[B].append(A)
    
    visited[0]=True # 예외상황 방지 : 0 방문 초기화
    dfs(1,visited) # 루트가 1이므로 1력터 시작
    for i in graph[2:]: # 2부터 마지막까지 출력
        print(i)

main()
