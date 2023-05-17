#계속 시간초과나서 블로그봄 ㅠㅠㅠ
#메모리 :65148 시간 :408
import sys
import heapq

input = sys.stdin.readline

n = int(input())
count = 0
liist = []
queue = []
for i in range(n):
    s, t = map(int, input().split())
    liist.append([s, t])
liist.sort(key=lambda x: x[0])

heapq.heappush(queue, liist[0][1])
for i in range(1, n):
    if queue[0] <= liist[i][0]:
        heapq.heappop(queue)
    heapq.heappush(queue, liist[i][1])
print(len(queue))


"""
classes = [[] for _ in range(n)]
visited = [0] * (n)

for i in range(n):
    s, t = map(int, input().split())
    liist.append([s, t])

# liist.sort(key=lambda x: (x[0], -x[1]))
liist.sort(key=lambda x: x[0])

for i in range(n):
    maxx = liist[i][1]
    if visited[i] == 0:
        classes[i].append(liist[i])
        visited[i] = 1
        count += 1

    for j in range(i + 1, n):
        if visited[j] == 0 and maxx <= liist[j][0]:
            visited[j] = 1
            classes[i].append(liist[j])
            maxx = liist[j][1]

print(count)
"""
