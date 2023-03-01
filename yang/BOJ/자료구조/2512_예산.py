# 32276KKB / 44ms
import sys
input = sys.stdin.readline
def solve():
    maxRequest = max(request)
    ans = 0 # 현재 배정한 예산
    sumRequest = 0 # ans 값으로 예산을 배정했을 때, 예산요청들의 합
    count = N # ans값으로 배정했을 때, 더 늘어날 수 있는 예산 요청의 수
    while sumRequest+count <= M: # 예산을 1 늘렸을 때 count값 만큼 늘어난다는 점 이용 // N<=M이므로 처음엔 무조건 통과하게 되어있음
        if count > 0:
            ans += (M - sumRequest)//count # (여유예산//count) 한 만큼을 추가로 예산에 배정
        else: break # count가 0이라는건 현재 더 나눠줄 수 있는 예산요청이 없다는 뜻
        
        if ans > maxRequest: # 배정되는 예산의 최댓값은 maxRequest값임
            ans = maxRequest
            break
        
        count = 0
        sumRequest = 0
        for r in request: # count와 sumRequest 계산
            if ans >= r:
                sumRequest += r
            else:
                sumRequest += ans
                count += 1
    return ans
N = int(input())
request = list(map(int, input().split()))
M = int(input())
print(solve())

'''
# test1
N = 4
request = [120, 110, 140, 150]
M = 485
if solve()!=127: print(f"test1 fail! {solve()}")

# test2
N = 5
request = [70, 80, 30, 40, 100]
M = 450
if solve()!=100: print(f"test2 fail! {solve()}")

# test3
N = 3
request = [1, 1, 1]
M = 3
if solve()!=1: print(f"test3 fail! {solve()}")

# test4
N = 4
request = [111, 111, 143, 153]
M = 323
if solve()!=80: print(f"test4 fail!  {solve()}")

# test5
N = 4
request = [1, 2, 3, 4]
M = 9
if solve()!=3: print(f"test5 fail!  {solve()}")
'''