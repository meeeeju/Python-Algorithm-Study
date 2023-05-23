# 32276KB / 96ms
n = int(input())
sign = list(input().split())
visited = [False]*10
ans = []
def dfs(number, p, temp):
    if p == len(sign):
        ans.append(temp)
    elif sign[p] == '<':
        for i in range(number+1, 10):
            if not visited[i]:
                visited[i] = True
                temp += str(i)
                dfs(i, p+1, temp)
                visited[i] = False
                temp = temp[:-1]
    else:
        for i in range(number):
            if not visited[i]:
                visited[i] = True
                temp += str(i)
                dfs(i, p+1, temp)
                visited[i] = False
                temp = temp[:-1]
for i in range(10):
    visited[i] = True
    dfs(i, 0, str(i))
    visited[i] = False
ans.sort()
print(ans[-1])
print(ans[0])