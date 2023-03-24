#	31388km /	44ms
import sys
from itertools import combinations, permutations
input = sys.stdin.readline

''' 
4 6 L C
a t c i s w'''
L , C = map(int,input().split())
chars = list(input().split())

vowel = ['a','e','i','o','u']

chars.sort()
combi_list = list(combinations(chars, L))
result =[]

for combi in combi_list:
    cnt =0
    for i in combi:
        if  i in vowel:
            cnt +=1
    if cnt >= 1 and L-cnt >= 2:
        result.append(combi)


for i in result:
    print("".join(i))
