# 58920KB / 192ms
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visit = list(map(int, input().split()))

ans = sum(visit[0:X])
candidate = sum(visit[0:X])
ans_count = 1
for start in range(1, N):
    end = start + X -1
    if end < N:
        candidate = candidate - visit[start-1] + visit[end]
        if candidate > ans:
            ans_count = 1
            ans = candidate
        elif candidate == ans:
            ans_count += 1
if ans == 0:
    print("SAD")
else:
    print(ans)
    print(ans_count)

# start = 0
# end = N-1
# while end-start+1 > X:
#     if visit[start] > visit[end]:
#         end -= 1
#     else:
#         start += 1
# ans = sum(visit[start:end+1])
# if ans == 0:
#     print("SAD")
# else:
#     print(ans)
