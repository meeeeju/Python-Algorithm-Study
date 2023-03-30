#블로그 참고
#메모리 :31256 시간 :72ms
import sys
input=sys.stdin.readline

p,m=map(int,input().split())
liist=[]

for i in range(p):
    I,n=input().split()
    if not liist:
        liist.append([[int(I),n]])
        continue
    enter=False
    for j in liist:
        if len(j)<m and j[0][0]-10<=int(I)<=j[0][0]+10:
            j.append([int(I),n])
            enter=True
            break
    if not enter:
        liist.append([[int(I),n]])

for j in liist:
    j.sort(key=lambda x:x[1])
for j in liist:
    if len(j)==m:
        print("Started!")
    else:
        print("Waiting!")
    for I,n in j:
        print(I,n)
