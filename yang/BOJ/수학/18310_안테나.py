# 블로그 참고
# 모든 집을 일렬로 나열했을때 중간에 있는 집이 최소
n =int(input())
s = list(map(int,input().split()))
s.sort()
if n%2==0: #  n이 짝수일때는 s[n//2]와 s[n//2-1]에 안테나를 설치 했을 경우에 합이 최소
    print(s[n//2-1]) # 더 작은 값을 출력하라고 했으니 s[n//2-1]을 출력
else: # n이 홀수일때는 s[n//2]
    print(s[n//2])