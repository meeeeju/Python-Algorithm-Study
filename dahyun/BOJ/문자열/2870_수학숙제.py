# 31256 KB / 44 ms
import sys
input = sys.stdin.readline
result=[]  # 모든 숫자들
for i in range(int(input())):
    n=input().strip()
    start='' # 숫자 문자열
    for j in range(len(n)):
        if n[j].isdigit():  # n[j]가 숫자일 경우
            if start=='': start=n[j]  
            else: start+=n[j]
        if n[j].isalpha() or j==len(n)-1:  # n[j]가 문자거나 문자열에서 마지막 문자라면
            if start=='': continue
            if start[0]=='0' and len(start)>1: result.append(int(start)) # start의 시작이 0이라면 빼고 result에 추가
            else: result.append(int(start))
            start=''
for re in sorted(result):  # 오름차순 정렬
    print(re)
