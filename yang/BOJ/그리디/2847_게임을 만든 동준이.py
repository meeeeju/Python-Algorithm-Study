# 31256KB / 44ms
import sys
input = sys.stdin.readline
n = int(input())
score = [0]
ans = 0
# for i in range(1, n+1):
#     score.append(int(input()))
#     if score[i-1] >= score[i]:
#         for k in range(i, 0, -1): # i~1
#             if score[k-1] >= score[k]:
#                 ans += score[k-1]-score[k]+1
#                 score[k-1] = score[k]-1

# for i in range(n):
#     score.append(int(input()))
# for i in range(n, 0, -1): # n~1
#     if score[i-1] >= score[i]:
#         for k in range(i, 0, -1): # i~1
#             if score[k-1] >= score[k]:
#                 ans += score[k-1]-score[k]+1
#                 score[k-1] = score[k]-1

for i in range(n):
    score.append(int(input()))
for i in range(n, 0, -1): # n~1
    if score[i-1] >= score[i]:
        ans += score[i-1]-score[i]+1
        score[i-1] = score[i]-1
print(ans)