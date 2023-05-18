#BeakJoon 2457 공주님의 정원
# 60620KB / 356ms
import sys
input = sys.stdin.readline
N=int(input())
flowers=[]
for i in range(N):
    sm, sd, em, ed = map(int, input().split())
    flowers.append([sm * 100 + sd, em * 100 + ed])
flowers.sort(key= lambda x:(-x[1],-x[0]))  # 내림차 정렬(꽃이 지는 날 기준)
s,f=0,0
count=0
min_s=10000
temps,tempf=0,0
for i in range(N):
    if (s==0 and flowers[i][1]<1200): break
    elif flowers[i][1]>=1200 and (flowers[i][1]-flowers[i][0]>f-s):   # 꽃이 지는 달이 12월이면 s,f 초기화
        s,f=flowers[i][0],flowers[i][1]
        temps,tempf=s,f
        count=1
    else:
        if flowers[i][1]<s: # 마지막 꽃이 피는 달(s)과 현재 꽃이 지는 달 사이 꽃이 피지 않는 요일 존재 
            if (not (s==temps and f==tempf) or (temps==0 and tempf==0)):
                s,f=temps,tempf  # 현재 이전까지는 꽃이 피지 않는 날이 없으므로, 이전 달의 값으로 초기화
                count+=1
                temps,tempf,min_s=s,f,10000
            else: break
        if flowers[i][1]>=s:  # 꽃이 필 수 있는 요일이 존재
            if min_s>flowers[i][0]:
                min_s=flowers[i][0]
                temps,tempf=flowers[i][0],flowers[i][1]
            if flowers[i][0]<=301:  # 꽃이 피는 달이 2월보다 작거나, 3월 1일 일 때 종료
                s,f=flowers[i][0],flowers[i][1]
                count+=1 
    if s<=301: break
if s>301: print(0)    
else: print(count)
