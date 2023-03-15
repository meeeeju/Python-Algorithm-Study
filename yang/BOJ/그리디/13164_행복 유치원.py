# 65132KB / 268ms
# 블로그 참고
# https://leesh111112.tistory.com/381
n, k = map(int, input().split())
heights = list(map(int, input().split()))
gaps = [heights[i] - heights[i-1] for i in range(1, n)]
gaps.sort(reverse=True)
print(heights[n-1]-heights[0]-sum(gaps[:k-1]))