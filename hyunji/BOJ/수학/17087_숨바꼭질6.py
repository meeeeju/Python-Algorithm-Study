#gcd안쓸려고 찾아봤지만 결국 gcd씀 ㅠ
#메모리 :44300 시간 :132ms
import sys
import math
input=sys.stdin.readline
N,S=map(int,input().split())
liist=list(map(int,input().split()))
liist2=[]

if N==1:
    print(liist[0]-S)
else:
    for i in range(len(liist)):
        liist2.append(abs(S-liist[i]))
    liist2.sort()
    num=liist2[0]
    for i in range(len(liist2)):
        num=math.gcd(liist2[i],num)
    print(num)
