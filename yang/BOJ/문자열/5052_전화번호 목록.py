# 질문게시판 참고
# 32276KB / 220ms

import sys
input = sys.stdin.readline
T = int(input())

def checkCons(numberList):
    numberList.sort(key=lambda x:(x,len(x)))
    # print(numberList)
    for i in range(N-1):
        if len(numberList[i])==len(numberList[i+1]): continue
        if numberList[i] == numberList[i+1][:len(numberList[i])]:
            return False
    return True

for _ in range(T):
    N = int(input())
    numberList = []
    for _ in range(N):
        numberList.append(input().rstrip())
    if not checkCons(numberList):
        print("NO")
    else:
        print("YES")
