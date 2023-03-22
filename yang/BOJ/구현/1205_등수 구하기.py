# 31256KB / 40ms
N, score, P = map(int, input().split())
if N==0 and P>0:
    print("1")
else:
    rank_list = list(map(int, input().split()))
    for i in range(N):
        if rank_list[i] > score:
            continue
        else:
            rank = i+1
            break
    else:
        rank = N+1
    if N+1 > P and rank_list[N-1]>=score:
        print("-1")
    else:
        print(rank)