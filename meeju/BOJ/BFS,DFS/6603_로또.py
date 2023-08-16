# 	31256	44
# 백트래킹으로 조합,순열 구하는 법 . 알려조 ~~
import sys
import itertools
input = sys.stdin.readline


'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0'''

while True:
    arr = list(map(int,input().split()))
    k = arr.pop(0)
    
    if k == 0:
        break
    kC6 = list(itertools.combinations(arr,6))

    for i in kC6:
        print(*i) 
    print()
    

