# 31256KB / 384ms
# 질문게시판 반례 참고!
# https://www.acmicpc.net/board/view/31853

n = int(input()) # 이동하려고 하는 채널
m = int(input()) # 고장난 버튼의 개수
def check(s):
    for i in str(s):
        if i in failure:
            return False
    return True
    # mod = 10
    # while s>0:
    #     if s%mod in failure:
    #         return False
    #     s = s//10
    # return True
failure = {}
if m > 0:
    # failure = set(map(int, input().split()))
    failure = set(input().split())

ans = abs(n-100)
plus_n, minus_n = n, n
while plus_n-n<ans:
    if check(plus_n):
        ans = min(ans, plus_n-n+len(str(plus_n)))
    if minus_n>=0 and check(minus_n):
        ans = min(ans, n-minus_n+len(str(minus_n)))
    plus_n += 1
    minus_n -= 1
print(ans)