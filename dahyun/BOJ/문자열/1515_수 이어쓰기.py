# 블로그 참고
# 31256 KB / 80 ms
import sys
input = sys.stdin.readline
nlist = input().strip()
i=0  # 증가하는 수
while True:
    i+=1
    num=str(i)  # num : 증가된 수를 문자열로 변환
    while len(num)>0 and len(nlist)>0:  # num과 nlist 모두 한자리 수 이상
        if num[0] == nlist[0]:  # num의 첫번째 자리와 nlist의 첫번째 자리가 같으면 nlist 맨 앞 빼주기
            nlist=nlist[1:]
        num=num[1:] # num의 모든 자리 수 다 확인해야하므로, num 하나씩 빼줌
    if nlist=='': # nlist가 비어졌을 때 i 출력 및 종료
        print(i)
        break
