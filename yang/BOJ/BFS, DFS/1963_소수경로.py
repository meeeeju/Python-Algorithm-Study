# 37560KB 192ms
import sys
from queue import Queue
def solution():
    A, B = input().split()
    A, B = A.strip(), B.strip()
    q = Queue()
    q.put((A, 0))
    visited = [False] * 10000
    while not q.empty():
        s, c = q.get()
        if s == B:
            print(c)
            break
        for i in range(4):
            for k in range(10):
                if i==0 and k==0:
                    continue
                temp = s[:i] + str(k) + s[i+1:]
                if not visited[int(temp)] and eratos[int(temp)]:
                    q.put((temp, c+1))
                    visited[int(temp)] = True
    else:
        print("Impossible")
        
input = sys.stdin.readline
eratos = [True] * 10000
for i in range(2, int(9999**0.5)+1):
    if eratos[i] == True:
        j = 2
        while i*j <= 9999:
            eratos[i*j] = False
            j += 1
T = int(input())
for _ in range(T):
    solution()