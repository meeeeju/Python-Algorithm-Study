# 31256KB / 48ms
import sys
input = sys.stdin.readline

# 백트래킹
def find(start):
    if len(lotto)==6:
        print(" ".join(lotto))
        return
    for i in range(start, k):
        if not visited[i]:
            visited[i] = True
            lotto.append(s[i])
            find(i+1)
            visited[i] = False
            lotto.pop()

# 입력받기
while True:
    line = input().rstrip().split()
    if line[0] == "0" : break
    k = int(line[0])
    s = line[1:]

    lotto = []
    visited = [False]*k
    find(0)
    print()