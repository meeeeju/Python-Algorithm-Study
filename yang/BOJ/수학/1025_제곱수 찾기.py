# 88ms / 31256 KB

import sys
input = sys.stdin.readline

def insertAns(a, b):
    for i in range(len(a)):
        ansSet.add(int(a[:i+1]))
        ansSet.add(int(a[i:]))
        ansSet.add(int(a[i]))
        ansSet.add(int(b[:i+1]))
        ansSet.add(int(b[i:]))
        ansSet.add(int(b[i]))

n, m = map(int, input().split())
table = []
for i in range(n):
    table.append(input().strip())

i, j = 0, 0 # 시작점
ansSet = set()
interval = 1

if n==1 and m==1:
    ansSet.add(int(table[0]))

while i+interval < n:
    for p in range(m): # 세로로 보는 경우
        temp = ""
        for x in range(i, n, interval):
            temp += table[x][p]
        if temp!= "" : insertAns(temp, temp[::-1])
    interval += 1
    if i+interval >= n:
        i = i+1
        interval = 1

while j+interval < m:
    for p in range(n): # 가로로 보는 경우
        temp = ""
        for x in range(j, m, interval):
            temp += table[p][x]
        if temp!= "" : insertAns(temp, temp[::-1])
    interval += 1
    if j+interval >= m:
        j = j+1
        interval = 1

for intervalN in range(0, n):
    for intervalM in range(0, m):
        if intervalN==0 and intervalM==0:continue
        for i in range(n): # 좌->우 대각선으로 보는 경우
            for j in range(m):
                d, a = i, j
                temp = ""
                while 0<=d<n and 0<=a<m:
                    temp += table[d][a]
                    d, a = d+intervalN, a+intervalM
                if temp!= "" : insertAns(temp, temp[::-1])
        for i in range(n): # 우->좌 대각선으로 보는 경우
            for j in range(m-1, -1, -1):
                d, a = i, j
                temp = ""
                while 0<=d<n and 0<=a<m:
                    temp += table[d][a]
                    d, a = d+intervalN, a-intervalM
                if temp!= "" : insertAns(temp, temp[::-1])

ans = -1 # 정답     
ansSet = sorted(list(ansSet), reverse=True)
for i in ansSet:
    if i**0.5==int(i**0.5):
        ans = max(ans, i)
        
print(ans)