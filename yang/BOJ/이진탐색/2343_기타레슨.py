# 42340KB / 204ms
# 블로그 참고
# start, end 범위 바꿔주니까 맞았음

def check(lectures, limit, M):
    count = 1
    temp = 0
    for lecture in lectures:
        if lecture > limit:
            return False
        temp += lecture
        if temp > limit:
            count +=1
            temp = lecture
    if count > M: return False
    else: return True

def solution2343(N, M, lectures):
    # start = 1
    start = max(lectures)-1
    end = sum(lectures)
    while start+1<end:
        mid = (start+end)//2
        if check(lectures, mid, M):
            end = mid
        else:
            start = mid
    return end
    
N, M = map(int, input().split())
lectures = list(map(int, input().split()))
print(solution2343(N, M, lectures))