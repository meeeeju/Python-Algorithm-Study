# 150336KB / 2076ms

def check(cut, treeHeights):
    amount = 0
    for treeHeight in treeHeights:
        if treeHeight > cut:
            amount += treeHeight-cut
    return amount
def solution_2805(N, M, treeHeights): 
    start, end = 0, max(treeHeights)
    while start+1<end:
        mid = (start+end)//2
        amount = check(mid, treeHeights)
        if amount>=M:
            start = mid
        else:
            end=mid
    return start
N, M = map(int, input().split()) 
treeHeights = list(map(int, input().split())) 
print(solution_2805(N, M, treeHeights))