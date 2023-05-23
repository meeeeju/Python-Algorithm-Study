#블로그 참고 data를 순열로 만들어서 그중에 체크한다는걸 생각하지 못함ㅠ..
#메모리 :31256 시간 :64
from itertools import combinations, permutations
import sys
input=sys.stdin.readline

n = int(input())
liist = []
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = list(permutations(data, 3))
# answer = []
count = 0

for i in range(n):
    number, strike, ball = map(int, input().split())
    liist.append([number, strike, ball])

liist.sort(key=lambda x: (-x[1], x[2]))

if liist[0][1] == 3:
    print(1)

else:
    for a in num:
        flag = 0
        for i in range(n):
            answer = list(map(int, str(liist[i][0])))
            strike, ball = 0, 0
            for j in range(3):
                if answer[j] == a[j]:
                    strike += 1
                elif a[j] in answer:
                    ball += 1

            if liist[i][1] != strike or liist[i][2] != ball:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            count += 1
print(count)
