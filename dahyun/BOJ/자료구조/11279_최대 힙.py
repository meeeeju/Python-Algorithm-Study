# 50156 KB / 316 ms
import sys
from queue import PriorityQueue
N=int(sys.stdin.readline())
PQ = PriorityQueue(maxsize=N)
for _ in range(N):
    x=int(sys.stdin.readline())
    if x!=0 : PQ.put((-x,x))
    elif not PQ.qsize() : print(0)
    else: print(PQ.get()[1])
        
