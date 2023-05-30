# 31256 KB / 40 ms
# 블로그 참고
N = int(input())
Gu = input().strip()
result=0
for i in range(1,N):
    if Gu[i-1]=='E' and Gu[i]=='W': result+=1
print(result)
