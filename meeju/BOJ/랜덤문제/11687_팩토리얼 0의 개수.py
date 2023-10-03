# 블로그 참고 
import sys
input = sys.stdin.readline

# 왜 right 초기값이 m*5를 해줘야되징?
'''블로그 코드 '''
def find_right_zeros(n):
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
    return zeros


m = int(input())
left, right, result = 1, m*5, 0


#  N!의 N을 찾기 위한 이진탐색
while left <= right:
    mid = (left + right) // 2

    # 메인 로직
    zero_count = find_right_zeros(mid)

    # 조건 분기
    if zero_count < m:
        left = mid + 1
    else:
        right = mid - 1
        result = mid

print(result if find_right_zeros(result) == m else -1)


# 5의 갯수만 신경쓰면 된다.
'''M = int(input())
num = 0
i=1
store = [0]
while M > 0:
    num = 5 * i
    M-=1
    store.append(1)
    if (i % 5)==0:
        store[i]+= store[i//5]
        M -=store[i//5]
    i+=1

if M ==0:
    print(5*(i-1))
else:
    print(-1)
'''

