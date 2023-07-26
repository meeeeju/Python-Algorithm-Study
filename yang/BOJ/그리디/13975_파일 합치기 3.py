# 블로그 참고
# 11066 파일합치기랑 뭐가 다르지??
import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    fileList = list(map(int, input().split()))
    heapify(fileList)
    result = 0
    # 가장 작은 2개의 파일 크기를 꺼내서 합친값을 다시 우선순위 큐에 넣기 
    while len(fileList) >= 2:
        f = heappop(fileList)
        s = heappop(fileList)
        result += (f + s)
        heappush(fileList, (f + s))
    print(result)