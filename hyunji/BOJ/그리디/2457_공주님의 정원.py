#블로그 참고
#메모리 :54476 시간 :2012
import sys
input=sys.stdin.readline

n = int(input())
liist = []
count = 0

for i in range(n):
    sm, sd, em, ed = map(int, input().split())
    liist.append([sm * 100 + sd, em * 100 + ed])

liist.sort(key=lambda x: (x[0], x[1]))

end = 301

while liist:
    if end >= 1201 or liist[0][0] > end:
        break
    tempend = 0
    for _ in range(len(liist)):
        if liist[0][0] <= end:
            if tempend <= liist[0][1]:
                tempend = liist[0][1]
            liist.remove(liist[0])
        else:
            break

    end = tempend
    count += 1
if end<1201:
    print(0)
else:
    print(count)
