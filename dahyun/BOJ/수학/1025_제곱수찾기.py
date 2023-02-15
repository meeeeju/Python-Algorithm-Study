#BackJoon 1025 제곱수 찾기
# 살짝 블로그 참고 (범위)
# 31256KB / 56ms
import sys
def search(x,y,n,m):
    text=str(table[x][y])
    if int(text)**0.5 == int(int(text)**0.5) : max=int(int(text)**0.5) # 들어온 값이 제곱이라면 max에 제곱근 값 저장
    else: max=-1  # 들어온 값이 제곱이 아니라면 max는 -1로 초기화
    while True:
        if 0<=x+n<N and 0<=y+m<M:  # n , m 만큼 이동했을 때 배열을 벗어나는지 확인
            text+=str(table[x+n][y+m])
            sqrt = float(text)**0.5  # 합쳐진 text 값의 제곱근
            if float(sqrt).is_integer() and max < sqrt : max=sqrt  # 구한 제곱근이 정수인지 확인 , max보다 클 경우 max에 방금 구한 제곱근 저장
            x+=n 
            y+=m
        elif max==-1 : return max # max가 -1이라면 모두 돌았을 때까지 제곱근이 존재하지 않았는 것이므로 -1 반환
        else: return int(max**2) # max 값은 제곱근이므로 max 제곱 반환


N,M = map(int,sys.stdin.readline().split())
table=[]
for _ in range(N):
    table.append(list(sys.stdin.readline().strip()))
if N==1 and M==1 and float(float(table[0][0])**0.5).is_integer() : max = table[0][0] # 들어온 값이 하나뿐이고, 제곱이라면 max에 table[0][0] 저장
else: max=-1
# x 인덱스 , y 인덱스 , x 이동범위 , y 이동범위 => 총 4번의 반복문
for i in range(N):
    for j in range(M):
        for n in range(-N,N):
            for m in range(-M,M):
                if m==0 and n==0 : continue # x의 이동범위 , y의 이동범위가 0이라면 무한루프에 빠지므로 조건문 걸어주기
                if 0<=i+n<N and 0<=j+m<M: # n , m 만큼 이동했을 때 배열을 벗어나는지 확인
                    r = search(i,j,n,m) 
                    if max<r : max=r # 전체 인덱스를 돌며 max 값 구하기
print(max)
