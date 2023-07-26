# 42340KB / 252ms

import sys
input = sys.stdin.readline

def check(size):
    count = 1
    tempSum = 0
    for l in lectureList:
        if tempSum+l <= size:
            tempSum += l
        else:
            tempSum = l
            count += 1
    if count > M: # size를 늘려야함
        return False
    return True # size를 줄여야함

N, M = map(int, input().split())
lectureList = list(map(int, input().split()))

start = max(lectureList)-1
end = sum(lectureList)
while (start+1<end):
    mid = (start+end)//2
    if check(mid): # size를 줄여도 됨 (가능)
        end = mid
    else: # size를 늘려야함 (불가능)
        start = mid
print(end)