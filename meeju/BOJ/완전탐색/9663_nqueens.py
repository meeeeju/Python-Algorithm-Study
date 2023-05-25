# Q1 재귀로 하게되면 시간 복잡도는 어떻게 계산하는 거지 ?


# 1. 같은 열에 있거나 k = i
# 2. 같은 행에 있거나 col[k] = col[i]
# 3. 같은 대각선 상에 있꺼나  col[k]-col[i] = k - i

N = int(input())    


col = [-1 for _ in range(N+1)] # 1 부터 N 까지로 보기
cnt = 0

def queens(i):
    global cnt 
    if ispromising(i):
        if i == N :
            cnt +=1
        else:
            for j in range(1,N+1):
                col[i+1]=j
                queens(i+1)

def ispromising(i):
    k = 1
    promise = True
    # while k < i :
    #     if col[i]==col[k] or abs(col[i]-col[k]) == abs(i-k):
    #         promise = False
    #         break
    #     k +=1

    for k in range(i-1,0,-1):
        if col[i]==col[k] or abs(col[i]-col[k]) == abs(i-k):
            promise = False
            break
    return promise


def main():
    queens(0)
    print(cnt)

main()