# 블로그 참조(https://latte-is-horse.tistory.com/370)
# 의문점 있음 : 9 7 3 1 6 10 13 s가 4인경우
import sys
input = sys.stdin.readline

n, nums = int(input()), list(map(int, input().split()))
s = int(input())

for i in range(n):
    # 탐색 
    max_num = max(nums[i: min(n, i + s + 1)]) # 현재 위치가 i 일 때 , i+s까지 탐색 가능하다. 슬라이싱할 시, i+s+1
    idx = nums.index(max_num)   # 바꿀 수 있는 가장 큰 수의 인덱스 번호 받기
    # 교환
    for j in range(idx, i, -1): # 자리 바꾸기
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
    # 후처리
    s -= (idx - i)  # 이동한 숫자 만큼 s 에서 차감시키기
    if s <= 0: break

print(*nums)

