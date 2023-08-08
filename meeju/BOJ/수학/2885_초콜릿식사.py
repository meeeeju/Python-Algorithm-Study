# 31256	40
'''6'''


def do_cutting(chocolate,K):    # 블로그 참고

    count = 0
    while K > 0:
        if K >= chocolate:
            K -= chocolate
        else:
            chocolate //= 2
            count += 1
    return count
            
def find_min_chocolate(K):

    s = 2
    while s < K:
        s *= 2 
    return s


K = int(input())      

if K == 1 :
    print(1, 0)
else:
    mini_chocolate = find_min_chocolate(K)
    if mini_chocolate == K :
        mini_cutting = 0
    else:
        mini_cutting = do_cutting(mini_chocolate,K)
    print(mini_chocolate,mini_cutting)
