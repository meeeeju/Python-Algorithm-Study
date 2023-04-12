#BaekJoon 9251 LCS
# 31388 KB / 224ms
#블로그 참고

A=input().strip()
B=input().strip()

lcs=[0]*len(B)
for a in range(len(A)):
    cnt=0   # 가장 큰 값
    for b in range(len(B)):
        if cnt<lcs[b]:  # 지금까지 증가하던 값이 lcs[b]보다 작으면 lcs[b]값으로 초기화 => 즉, 지금까지 구한 최댓값
            cnt=lcs[b]
        elif A[a]==B[b]:
            lcs[b]=cnt+1
print(max(lcs))

            
            
    
