# 32276 KB / 160 ms
# 문제 이해가 안돼서 질문 게시판 참고
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    call = [input().strip() for _ in range(n)]
    call.sort() # 모든 전화번호 정렬
    for i in range(n-1):
        if call[i]==call[i+1][:len(call[i])]: print("NO"); break  # 현재 전화번호와 다음 전화번호가 일치할 경우를 찾음
    else: print("YES")
