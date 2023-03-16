# 42340KB / 184ms
# 왜 틀렸는지 계속 몰랐는데
# 질문게시판에 이거 보고 알았음! https://www.acmicpc.net/board/view/90474

import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))

subSum = [honey[0]] + [0]*(n-1)
for h in range(1, n):
    subSum[h] = subSum[h-1]+honey[h]
def customSum(start, end): # (start, end] 까지의 합
    if start == -1 : return subSum[end]
    return subSum[end]-subSum[start]

# 꿀통이 가운데에, 벌들 양쪽 끝에
maxHoneySum = customSum(0, n-2) + max(honey[1:n-1])

for i in range(1, n-1): # i는 두번째 별의 위치 : 1~n-2
    # 벌들 왼쪽에, 꿀통 오른쪽 끝에 -> 첫번째벌은 0, 꿀통은 n-1
    honeySumLeft = customSum(0, i-1) + 2*customSum(i, n-1)
    
    # 벌들 오른쪽에, 꿀통 왼쪽 끝에 -> 첫번째벌은 n-1, 꿀통은 0
    honeySumRight = customSum(i, n-2) + 2*customSum(-1, i-1)
    
    maxHoneySum = max(maxHoneySum, honeySumLeft, honeySumRight)

print(maxHoneySum)