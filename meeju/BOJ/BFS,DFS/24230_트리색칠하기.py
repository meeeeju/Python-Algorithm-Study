# 블로그 참고 / 질문 게시판 참고
# 83016KB / 1184ms

import sys
from queue import Queue
input = sys.stdin.readline


def tint_color(s,graph,current,stated):

    visited = [False for _ in range(V+1)]
    queue = Queue()
    queue.put(s)
    visited[s]=True
    count = 0

    while (queue.qsize()>0):
        v = queue.get()
        for w in graph[v]:
            if not visited[w]:
                visited[w]=True
                if stated[w-1] != stated[v-1]:
                    # stated[w-1] = stated[w-1]
                    count +=1
                queue.put(w)
    return count


V = int(input())      # 정점 수 
E = V - 1       # 간선 수 
stated_color_list = list(map(int,input().split()))  # 입력 받은 색깔 리스트 
current_color_list = list(0 for _ in range(V))  # 전부 흰색으로 초기화 

tree = [[] for _ in range(V+1)]
for _ in range(E):
    v,w = map(int,input().split())
    tree[v].append(w)
    tree[w].append(v)

result = tint_color(1,tree,current_color_list,stated_color_list)

if  stated_color_list[0] != 0:
    result +=1

print(result)



