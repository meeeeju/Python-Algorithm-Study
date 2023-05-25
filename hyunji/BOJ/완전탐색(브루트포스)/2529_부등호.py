# 시간 너무 많이 걸리길래 블로그보니 dfs 하는걸 봄!!
# 메모리 :32276 시간 :184
import sys
input=sys.stdin.readline

k = int(input())
liist = list(input().split())
result = []


def dfs(n, number):
    if n >= k:
        result.append(number)
        return
    for i in range(10):
        if not str(i) in number:
            if liist[n] == "<":
                if int(number[-1]) < i:
                    dfs(n + 1, str(number) + str(i))

            elif liist[n] == ">":
                if int(number[-1]) > i:
                    dfs(n + 1, str(number) + str(i))

    return


for i in range(10):
    dfs(0, str(i))
print(result[-1])
print(result[0])


"""
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = list(permutations(data, k + 1))
answer = []
delete = []
number = []
for i in range(len(num)):
    number.append(list(num[i]))

for i in range(len(number)):
    for j in range(len(liist)):
        if liist[j] == "<":
            if number[i][j] >= number[i][j + 1]:
                delete.append(number[i])
                break
        elif liist[j] == ">":
            if number[i][j] <= number[i][j + 1]:
                delete.append(number[i])
                break

sub = [x for x in number if x not in delete]
print(sub[-1])
print(sub[0])"""
