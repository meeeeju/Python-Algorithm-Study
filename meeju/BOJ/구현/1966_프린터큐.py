# 	37120	116
import sys
from collections import deque
from queue import Queue
input = sys.stdin.readline

'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1'''


def printQueue(document):


    q = deque(document)
    cnt = 0
    while q:
        max_element = max(q)
        element = q.popleft()
        
        if element[0] < max_element[0] :
            q.append(element)
        else:
            cnt +=1
            if element[1] == M :
                return cnt 
        
T = int(input())

for _ in range(T):
    N, M = map(int,input().split()) # 문서의 갯수, 몇 번째

    document = list(map(int,input().split()))
    for i in range(N):
        document[i] = (document[i],i)
    print(printQueue(document))
