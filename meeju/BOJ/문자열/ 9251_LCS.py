# DP 로 풀어야된다,,? 는 것까지만 혼자 생각했음,,! -> 어떤식으로 로직 접근 해야될지 몰라서 블로그 참고
import sys
input = sys.stdin.readline

'''
ACAYKP
CAPCAK'''

# 2차원 배열의 캐시를 만들어서 해결

word1, word2 = input().strip(),input().strip()

h,w= len(word1),len(word2)

cache = [[0]*(w+1) for _ in range(h+1)]

for i in range(1,h+1):
    for j in range(1,w+1):
        if word1[i]==word2[j]:
            cache[i][j]= cache[i-1][j-1]+1
        else:
            cache[i][j]= max(cache[i][j-1],cache[i-1][j])
print(cache[-1][-1])