# 31256KB/	48ms
# 블로그 참고 - 문제 이해 잘못함
k=int(input())
dp = 1
choco = 0 # 최소 크기의 초콜릿
count = 0 # 최소 몇 번 쪼개
for i in range(1,30):
    if dp*2==k: 
        print(k,0)
        exit(0)
    elif dp*2>k: 
        choco = dp*2
        break
    else: dp*=2
print(choco, end=" ")
while True:
    if k%choco==0: # 나누어떨어지는지,,
        print(count)
        break
    else:  
        choco//=2
        count+=1

