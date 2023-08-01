# 37% 에서 틀림

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trains = [set() for _ in range(N+1)]
for _ in range(M):
    command = tuple(map(int, input().split()))
    if command[0]==1:
        i, x = command[1], command[2]
        trains[i].add(x)
    elif command[0]==2:
        i, x = command[1], command[2]
        if x in trains[i]:
            trains[i].remove(x)
    elif command[0]==3:
        i = command[1]
        temp = set()
        for t in trains[i]:
            if t+1 <= 20 : temp.add(t+1)
        trains[i] = temp
    elif command[0]==4:
        i = command[1]
        temp = set()
        for t in trains[i]:
            if t-1 >= 1 : temp.add(t-1)
        trains[i] = temp
        
result = set()
for i in range(1, N):
    t = tuple(sorted(trains[i]))
    if t not in result:
        result.add(t)
print(len(result))

#https://e-you.tistory.com/390
'''
n,m = map(int,input().split())

train = [[0 for _ in range(20)] for _ in range(n)]

for i in range(m):
    arr = list(map(int,input().split()))
    if arr[0] == 1:
        train[arr[1]-1][arr[2]-1] = 1
    elif arr[0]==2:
        train[arr[1]-1][arr[2]-1] = 0
    elif arr[0]==3:
        train[arr[1]-1].insert(0,0)
        train[arr[1]-1].pop()
    else:
        train[arr[1]-1].pop(0)
        train[arr[1]-1].append(0)

tmp = []
for t in train:
    if t not in tmp:
        tmp.append(t)
print(len(tmp))
'''