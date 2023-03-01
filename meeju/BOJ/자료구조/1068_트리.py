# 31388kb /	44ms
import sys
input = sys.stdin.readline


def main():

    N = int(input())    # 노드의 갯수
    tree =list(map(int,input().split()))    # 각 노드의 부모
    removal = int(input())  # 제거 노드

    # 트리 만들어주기(부모)
    for i in range(N):
        tree[i]=(tree[i],[])

    # 루트가 리프노드라면 조기 종료
    if tree[removal][0] ==-1:
        print(0)
        return
    
    # 트리 만들어주기(자식)
    for i in range(N):
        if tree[i][0] >= 0:
            tree[tree[i][0]][1].append(i)

    def dfs(graph,s):

        def recur(v):
            visited.append(v)
            for i in graph[v][1]:
                recur(i)

        visited=[]
        recur(s)
        return visited
    
    removal_tree = dfs(tree,removal)    # 제거 노드 트리 탐색
    count = 0  # 리프 노드의 갯수 
    for i in range(N):
        if not i in removal_tree:
            if i == tree[removal][0]:   # 제거 노드의 부모에 해당된다면 
                tree[i][1].remove(removal)  # 제거 노드 제거
            if not tree[i][1]:  # 리프 노드인 경우
                count +=1
    
    print(count)


main()