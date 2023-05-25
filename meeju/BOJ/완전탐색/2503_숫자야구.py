# 블로그 참고 : https://yuna0125.tistory.com/115
# 문제 접근 방식이 완전히 틀렸다. 
# 내 접근 방식은 민혁이가 추측한 수들로부터 가능한 모든 숫자들을 만들어 나가는 방식 ( 재귀 )
# 완전 탐색인 만큼 진짜 가능한 경우를 모두 완전 탐색해줘야함
# permutation 외우기 

'''
4
123 1 1
356 1 0
327 2 0
489 0 1
'''

from itertools import permutations
N = int(input()) # 추측 횟수 

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))   # 1~9로 만들 수 있는 가능한 모든 수의 순열

for _ in range(N):
    n, s, b = map(int, input().split()) # 수, 스트라이크, 볼 여부
    n = list(str(n))
    rmcnt = 0
    for i in range(len(num)):   # 가능한 모든 경우의 수 돌려주기 
        strike = ball = 0
        i -= rmcnt # num[0] 부터 시작
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1
            
        if (strike != s) or (ball != b):
            num.remove(num[i])  # 리스트에서 num[i] 완전 삭제 
            rmcnt += 1

print(len(num))
