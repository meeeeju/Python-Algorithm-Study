#  블로그 참고 / 질문 게시판 참고 -> 개멍청,,,10007로 안 나눠줌 ㅠ 문제 잘 보장,,,!!
#  31256KB / 44ms
import sys
input = sys.stdin.readline

# 입력 : 가로의 길이 (width)
# 출력 : 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수

# 입력받기
width = int(input())

def main():

    # 초기화
    dp = [0 for _ in range(width+1)] # 1 ~ width
    dp[0]=1
    dp[1]=1

    if width ==1 :
        print(dp[width]%1007)
        return
        
    for i in range(2,width+1):
        dp[i] = dp[i-2] + dp[i-1]
        
    print(dp[width]%10007)

    return
main()


