# 34488kb / 816ms
import sys
from collections import deque
input = sys.stdin.readline

def add(heap,x,i):  # swim up

    heap.append(x) 
    while (i>1):
        if heap[i] > heap[i//2]:
            heap[i],heap[i//2] = heap[i//2],heap[i]
            i = i//2
        else:
            break
    return

def get_max(heap):  # sink(swim down)

    if len(heap) == 1:
        return 0
    
    if len(heap) ==2:
        return heap.pop()

    max = heap[1]
    heap[1]= heap.pop()

    i=1
    while(2*i <= len(heap)-1 ):
        if 2*i+1 > len(heap)-1:
            j = 2 * i
        elif heap[2*i] >= heap[2*i+1]:
            j = 2*i
        else:
            j = 2*i +1
    
        if (heap[i]< heap[j]):      # 꼭대기에서부터 아래로
            heap[i],heap[j] = heap[j],heap[i]
            i = j 
        else:
            break

    return max

N = int(input())
heap =deque([0])

for _ in range(N):

    x = int(input())
    if x :
        add(heap,x,len(heap))
    else:
        print(get_max(heap))



