# 31256KB / 40ms
from itertools import combinations
L, C = map(int, input().split())
alpha = sorted(input().split())
ans = combinations(alpha, L)
vowel = {'a', 'e', 'i', 'o', 'u'}
for a in ans:
    s = ""
    consonants_count = 0
    vowels_count = 0
    for i in a:
        if i in vowel:
            vowels_count += 1
        else:
            consonants_count += 1
        s+=i
    if consonants_count>=2 and vowels_count>=1:
        print(s)