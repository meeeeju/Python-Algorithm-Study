# 31256 KB / 44 ms
import sys
input = sys.stdin.readline
nlist=[]
for _ in range(int(input())):
    nlist.append(list(map(int,input().split())))
count=0
for i in range(1,10):  # 첫번 째
    for j in range(1,10): # 두번 째
        if i==j : continue
        for k in range(1,10): # 세번 째
            result=True
            if i==k or j==k : continue
            for number,s,b in nlist:
                t1,t2,t3=str(number)  # 민혁이가 물어본 숫자 3개
                i1,i2,i3=str(i),str(j),str(k) # 조합된 숫자 3개
                ts,tb=0,0  # test strike , test ball
                if i1==t1 : ts+=1  # 같은 숫자, 같은 위치이면 ts 1증가
                if i2==t2 : ts+=1
                if i3==t3 : ts+=1
                if i1==t2 or i1==t3 : tb+=1 # 같은 숫자, 다른 위치이면 tb 1증가
                if i2==t1 or i2==t3 : tb+=1
                if i3==t1 or i3==t2 : tb+=1
                if ts!=s or tb!=b : result=False; break  # 영수가 답한 s와 t값과 ts,tb이 다르면 i1,i2,i3은 아예 틀린 값이므로 break
            if result: count+=1  # 조합된 숫자가 모든 조건을 통과할 때 count 증가 
print(count)
                
