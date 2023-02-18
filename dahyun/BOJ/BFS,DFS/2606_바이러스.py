# 31256 KB / 44 ms
import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 늘려주기
def dfs(index):  # dfs로 index와 연결되어 있는 노드 돌기
    visited[index]=True
    for g in graph[index]:
        if visited[g] : continue
        else : 
            dfs(g)
    return   
    
def main():    
    global graph
    global visited
    
    computer_num=int(sys.stdin.readline())
    graph=[[] for _ in range(computer_num+1)]
    visited=[False for _ in range(computer_num+1)]

    for _ in range(int(sys.stdin.readline())):
        A,B = map(int,sys.stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    dfs(1)
    
    print(visited.count(True)-1) # visited에 True(방문했던 노드들)가 표시된 인덱스 개수 구하기

main()
    
