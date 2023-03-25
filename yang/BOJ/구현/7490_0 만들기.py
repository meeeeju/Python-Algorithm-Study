# 백트래킹 설명 찾아봄
# 31256KB / 44ms

import sys
input = sys.stdin.readline

def find(n):
    def previous(s):
        for i in range(len(s)-1, -1, -1):
            if s[i] == '+' or s[i] == '-':
                break
        return int(s[i:].replace(" ", ""))
    def recur(formula, position, calcul):
        if position == n-1:
            if calcul == 0: result.append(formula)
            return
        next = position+1
        num = previous(formula)
        new_calcul = calcul-num+num*10
        new_calcul = new_calcul + arr[next] if num>0 else new_calcul-arr[next]
        recur(formula+' '+str(arr[next]), next, new_calcul)
        recur(formula+'+'+str(arr[next]), next, calcul+arr[next])
        recur(formula+'-'+str(arr[next]), next, calcul-arr[next])
        
    arr = [i for i in range(1, n+1)]
    result = []
    recur('1', 0, 1)
    return result
    

T = int(input())
ans = {}
for _ in range(T):
    N = int(input())
    if not N in ans:
        ans[N] = find(N)
    print('\n'.join(ans[N]))
    print()