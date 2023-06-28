# 블로그 참고
import sys
input = sys.stdin.readline

'''
5 N
2 1 5 4 3 배열 hi'''

''' 시간 초과
N = int(input())
ballon_list = list(map(int,input().split()))
survive_list = [True for _ in range(N)]

arrow = 0 
for j in range(N): 
    target = ballon_list[j]   
    if survive_list[j] :    # 생존 중이면
        arrow +=1
        survive_list[j]=False
        target -= 1
        for i in range(j+1,N):
            if ballon_list[i] == target and survive_list[i]: # 생존 중이면
                survive_list[i]=False
                target -=1
        

            
print(arrow)
'''




n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
# 발사된 각 화살의 높이
cnt = [0] * (n + 1)

# 화살의 높이를 확인한다.
for i in h:
    # 화살이 발사되어있으면 똑같은 화살로 풍선을 터트리고 화살의 높이를 내린다.
    if cnt[i] > 0:
        # 풍선을 터트리고 원래 화살을 빼주고
        # 화살의 높이 -1 위치에 화살을 다시 조준한다.
        cnt[i] -= 1
        cnt[i - 1] += 1
    else:
        # 화살이 발사되지 않았으므로
        # 풍선을 터트리고 화살의 높이 -1 위치에 화살을 조준한다.
        cnt[i - 1] += 1

# 발사된 화살의 개수를 출력한다.
print(sum(cnt))
