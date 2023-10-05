# 블로그 참고

def multi_count(n):
    count = 0
    while n >= 5:
        n = n//5
        count += n
    return count
    

M = int(input())

start = 1
end = M * 5
is_ans = False
while start<=end:
    mid = (start+end)//2
    if multi_count(mid) < mid:
        start = mid + 1
    else:
        end = mid - 1
        is_ans = True

if is_ans:
    print(start)
else:
    print(-1)