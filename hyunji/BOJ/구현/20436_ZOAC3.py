#메모리 :31256 시간 :40
import sys

input = sys.stdin.readline

sl, sr = input().split()
liist = list(input())
lefttime = 0
righttime = 0
liistzip = []
leftzip = []
rightzip = []
keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
right = ["yuiophjklbnm"]
left = ["qwertasdfgzxcv"]

for i in range(len(keyboard)):
    if sl in keyboard[i]:
        slx = i
        sly = keyboard[i].index(sl)
    if sr in keyboard[i]:
        srx = i
        sry = keyboard[i].index(sr)

for i in range(len(liist)):
    for j in range(len(keyboard)):
        if liist[i] in keyboard[j]:
            liistzip.append([j, keyboard[j].index(liist[i])])

for i in range(len(liist)):
    for j in range(len(left)):
        if liist[i] in left[j]:
            leftzip.append(liistzip[i])

for i in range(len(liist)):
    for j in range(len(right)):
        if liist[i] in right[j]:
            rightzip.append(liistzip[i])

for i in range(len(leftzip)):
    lefttime += abs(slx - leftzip[i][0]) + abs(sly - leftzip[i][1])
    slx = leftzip[i][0]
    sly = leftzip[i][1]

for i in range(len(rightzip)):
    righttime += abs(srx - rightzip[i][0]) + abs(sry - rightzip[i][1])
    srx = rightzip[i][0]
    sry = rightzip[i][1]

print(lefttime + righttime + (len(liist) - 1))
