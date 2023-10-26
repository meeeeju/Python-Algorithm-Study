# 구현 힘들다,,,
# 178ms / 41.77Mb

import sys
from collections import deque
input = sys.stdin.readline

H, K, R = map(int, input().split())

total_node_count = 2**(H+1) - 1
last_node_count = 2**H
waiting_job = []

for _ in range(last_node_count):
    waiting_job.append(list(map(int, input().split())))

class Node:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def have_job(self):
        if len(self.left) > 0 or len(self.right) > 0:
            return True
        return False

tree = [Node() for _ in range(total_node_count + 1)]

k = 0
ans = 0
last_start = total_node_count - last_node_count + 1
last_end = total_node_count
for day in range(1, R+1):
    # root node
    if tree[1].have_job():
        if day % 2 == 0 and tree[1].right: # 짝수 날짜에는 오른쪽 부하 직원이 올린 업무 처리
            ans += tree[1].right.popleft()
        elif day % 2 == 1 and tree[1].left: # 홀수 날짜에는 왼쪽 부하 직원이 올린 업무 처리
            ans += tree[1].left.popleft()

    # 가운데 노드 처리
    start = 2
    end = 3
    current_line = 2 # 현재 높이의 노드 수
    while current_line < last_node_count:
        for i in range(start, end + 1): # 업무를 처리해서 상사에게 올림
            if tree[i].have_job():
                if day % 2 == 0 and tree[i].right: # 짝수 날짜 -> 오른쪽 업무 처리
                    if i % 2 == 0: # 내가 왼쪽 부하직원
                        tree[i//2].left.append(tree[i].right.popleft()) # 상사의 왼쪽에 내 오른쪽 업무를 넣음
                    else: # 내가 오른쪽 부하 직원
                        tree[i//2].right.append(tree[i].right.popleft()) # 상사의 오른쪽에 내 오른쪽 업무를 넣음
                elif day % 2 == 1 and tree[i].left: # 홀수 날짜 -> 왼쪽 업무 처리
                    if i % 2 == 0: # 내가 왼쪽 부하직원
                        tree[i//2].left.append(tree[i].left.popleft()) # 상사의 왼쪽에 내 왼쪽 업무를 넣음
                    else: # 내가 오른쪽 부하 직원
                        tree[i//2].right.append(tree[i].left.popleft()) # 상사의 오른쪽에 내 왼쪽 업무를 넣음
        current_line *= 2
        start = end + 1
        end = start + current_line - 1
    if k >= K:
        continue
    # leaf node 처리
    for i in range(last_start, last_end + 1):
        if i % 2 == 0: # 내가 왼쪽 부하 직원
            tree[i//2].left.append(waiting_job[i-last_start][k])
        else: # 내가 오른쪽 부하 직원
            tree[i//2].right.append(waiting_job[i-last_start][k])
    k += 1

print(ans)