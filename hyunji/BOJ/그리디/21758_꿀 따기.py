#메모리 :42340 시간 :196ms
#블로그 참고

import sys
input=sys.stdin.readline

N=int(input())
honey=list(map(int,input().split()))
max_honey=0
summ=sum(honey[:])
temp=honey[0]

#벌-꿀-벌
for i in range(1,N):
    max_honey=max(max_honey,summ-honey[0]-honey[-1]+honey[i])

#벌-벌-꿀
for i in range(1,N):
    temp+=honey[i]
    max_honey=max(max_honey,summ-honey[0]+summ-temp-honey[i])

#꿀-벌-벌
honey.reverse()
temp=honey[0]
for i in range(1,N):
    temp+=honey[i]
    max_honey=max(max_honey,summ-honey[0]+summ-temp-honey[i])
print(max_honey)
