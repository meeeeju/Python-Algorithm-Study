#BaekJoon 1969 DNA
# 31256 KB / 56 ms
import sys
input = sys.stdin.readline
N,M = map(int,input().split()) # N : DNA 개수 , M : 문자열 길이
DNA=[] # DNA 저장 리스트
for _ in range(N): DNA.append(input().strip())
result1='' # Hamming Distance의 합이 가장 작은 DNA
result2=0 # Hamming Distance의 합
for i in range(M):  
    max_name=dict() # DAN[j][i] 위치의 뉴클레오티드 개수
    for j in range(N):
        if DNA[j][i] in max_name: max_name[DNA[j][i]]+=1
        else: max_name[DNA[j][i]]=1
    result=sorted(max_name.items(), key = lambda item: (-item[1],item[0]))[0] # 가장 큰 개수의 뉴클레오티드, 사전 순으로 정렬
    result2+=(N-result[1]) # DNA 개수 - 선택된 뉴클레오티드의 개수
    result1+=result[0] # 선택된 뉴클레오티드
print(result1)
print(result2)

'''
DNA 문자열의 i 위치에 있는 뉴클레오티드들의 개수를 구함
-> 가장 큰 개수를 가진 뉴클레오티드를 선택
'''
