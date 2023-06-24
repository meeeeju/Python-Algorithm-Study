# 블로그 코드

import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))

floating = [0] * 1000001 # 현재 떠있는 화살의 개수

# O(n) 풀이
for height in heights:
    # 해당 높이에서 떠 있는 화살이 있다면,
    if floating[height] > 0:
        # 그 화살 중 하나를 바로 아래 높이로 이동시킨다.
        floating[height] -= 1
        floating[height - 1] += 1
    # 해당 높이에서 떠 있는 화살이 없다면, 화살을 쏜다. 일단, 맞췄으니까 바로 높이를 -1한다.
    else:
        floating[height - 1] += 1

# 남아 있는 화살의 총합이 답이다. o(n)
print(sum(floating))