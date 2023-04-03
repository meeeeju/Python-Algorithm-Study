#블로그참고
# 아,, 내가 생각한 방법대로 했는데,,, 계속 틀렸습니다. 떠서 그냥 블로그 봤는데 접근 방법이 다르더라구,,어렵다,,
N, D = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
dis = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        dis[i] = min(dis[i], dis[i-1]+1)
    for s, e, d in li:
        if i == s and e <= D and dis[i]+d < dis[e]:
            dis[e] = dis[i]+d
print(dis[D])
