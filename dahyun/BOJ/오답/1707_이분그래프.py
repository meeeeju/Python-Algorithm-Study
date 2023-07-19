# 블로그참고
# 53516KB / 1328 ms
import sys
sys.setrecursionlimit(100000000)
input=sys.stdin.readline
def dfs(n,color_num):  # n : node, color_num : 색칠 번호 (1,-1 로 구분)
    global bipartite_graph
    color[n]=color_num
    for g in graph[n]:
        if color[g]==0 : dfs(g,color_num*-1)  # 색칠 되지 않았다면 dfs 넣어줌 , 이때 color_num은 -1을 곱해서 넘겨줌
        elif color[g]==color_num: # 만약 n과 연결된 노드의 색이 n과 같다면 이분그래프가 아님 !
            bipartite_graph=False
            return
        
    
for _ in range(int(input())):
    V,E = map(int,input().split())
    color = [0 for _ in range(V+1)]  # 해당 노드의 색을 나타내는 리스트
    graph=[[] for _ in range(V+1)] # 연결된 그래프
    bipartite_graph=True  # 이분그래프인지 판별
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,V+1):
        if color[i]==0: dfs(i,1)  # 색칠되지 않은 노드를 찾아 dfs 돌림
    if bipartite_graph : print("YES")  # 이분그래프일 때
    else: print("NO")  # 이분그래프 아닐 때

'''
1
5 2
1 2
2 3
-> YES

1
4 2
1 2
3 4
-> YES

1
4 3
1 4
2 3
3 4
-> YES

1
5 4
1 2
3 4
3 5
4 5
-> NO
'''
