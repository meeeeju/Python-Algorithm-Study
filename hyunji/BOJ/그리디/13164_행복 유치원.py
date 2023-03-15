#메모리 :66737 시간 :352ms
#블로그 참고
import sys
input=sys.stdin.readline

N,K=map(int,input().split())
children=list(map(int,input().split()))
liist=[]

for i in range(N-1):
    liist.append(children[i+1]-children[i])
liist.sort()
print(sum(liist[:N-K]))
