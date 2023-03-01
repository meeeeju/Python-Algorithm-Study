# 32276KKB / 44ms
import sys
input = sys.stdin.readline
def solve():
    maxRequest = max(request)
    sumRequest = 0
    ans = 0
    count = N
    while sumRequest+count <= M:
        if count > 0:
            ans += (M - sumRequest)//count
        else: break
        if ans > maxRequest:
            ans = maxRequest
            break
        count = 0
        sumRequest = 0
        for r in request:
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