import sys
input = sys.stdin.readline
'''
5 8 N(dna 수) M(문자열의 길이)
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT


TAAGATAC
7 (Hamming Distance)
'''


N, M = map(int,input().split())
dna_list =[ 0 for _ in range(N)]


common_chr= [[] for _ in range(M)]

for i in range(N):
    dna_list[i]=input().rstrip()


for dna in dna_list:
    for i in range(M):
        common_chr[i].append(dna[i])

res =''
res_cnt = []
for j in range(M):

    visited =[]
    max_a = common_chr[j][0]
    max_cnt = 0
    for i in range(N):
        alpha = common_chr[j][i]
        if alpha not in visited:
            if common_chr[j].count(alpha) > max_cnt:
                max_cnt=common_chr[j].count(alpha)
                max_a=alpha
            elif common_chr[j].count(alpha) == max_cnt:
                max_a = min(alpha,max_a )
        visited.append(alpha)
    
    res_cnt.append(max_cnt)
    res += max_a

hamming_distance = 0
for cnt in res_cnt:
    hamming_distance += (N-cnt)

print(res)
print(hamming_distance)
