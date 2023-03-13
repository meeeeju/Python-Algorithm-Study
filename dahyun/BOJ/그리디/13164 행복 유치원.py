# 66736 KB / 264 ms
# 블로그 참고
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
tall_list=list(map(int,input().split()))
tall_dif=[]

for i in range(N-1):  # 각 원생 키의 차이들을 저장
    tall_dif.append(tall_list[i+1]-tall_list[i])
tall_dif.sort()
print(sum(tall_dif[:N-K]))
