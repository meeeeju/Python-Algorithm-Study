#출력형식이 잘못되었다고 해서 질문게시판 참고
#메모리 :85900 시간 :948
import sys
input=sys.stdin.readline

n=int(input())
liist=[]
liist2=[]
result=dict()
for _ in range(n):
    liist.append(list(input()))

for i in range(n):
    for j in range(len(liist[i])):
        if liist[i][j]=='.':
            liist2.append(''.join(liist[i][j+1:]))

for i in liist2:
    if i in result:
        result[i]+=1
    else:
        result[i]=1

result=sorted(result.items())
for i in range(len(result)):
    print(str(result[i][0]).rstrip(),str(result[i][1]).rstrip())
