#31256KB/	48ms
# 블로그 참고 
import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
S=int(input())
for i in range(N): # 현재 위치 
    m=A.index(max(A[i:min(N,i+S+1)])) # A의 범위에서 가장 큰 숫자의 인덱스를 찾음
    for j in range(m,i,-1): # 현재위치(i) ~ 가장 큰 값 위치(m) 사이 모두 swap
        A[j],A[j-1]=A[j-1],A[j]
    S-= m-i  # 현재 위치(i) ~ 가장 큰 값 위치(m) 값을 S에서 빼줌
    if S<=0: break
print(*A)
