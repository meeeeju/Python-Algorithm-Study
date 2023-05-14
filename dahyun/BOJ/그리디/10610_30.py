#BaekJoon 10610 30
# 32388 KB / 104 ms
nlist = input().strip()
nlist="".join(sorted(nlist,reverse=True))  # 문자열 정렬
if nlist[-1]!='0': print(-1)  # 문자열의 마지막이 0이 아니면 -1 출력
else: 
    if int(nlist[:len(nlist)-1])%3==0: print(nlist)  # 0을 제외한 수가 3의 배수면 출력
    else: print(-1)
   
'''
nlist = input().strip()
nlist="".join(sorted(nlist,reverse=True))
if nlist[-1]!='0': print(-1)
else: 
    if int(nlist)%30==0: print(nlist)
    else: print(-1)
'''
