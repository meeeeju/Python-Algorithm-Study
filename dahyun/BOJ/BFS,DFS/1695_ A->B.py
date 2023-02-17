# 31256KB / 80ms

import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 늘려주기
def dfs(a,b,count):
    if a>=b: return a, count  # a가 b보다 크다면 리턴 
    temp_a1 , t_c1 = dfs(a*2,b,count+1) # a에 2를 곱하기한 후 재귀
    temp_a2 , t_c2 = dfs(int(str(a)+'1'),b,count+1) # a 뒤에 1 추가 후 재귀
    if temp_a1 == b and temp_a2 ==b:  # 두 상황 둘 다 b와 같다면 count 값이 더 작은 수로 리턴
        if t_c1<t_c2 : return temp_a1,t_c1
        else : return temp_a2, t_c2
    elif temp_a1 == b : return temp_a1, t_c1 # a*2 값과 b가 같다면 리턴
    elif temp_a2 == b : return temp_a2, t_c2 # a 뒤에 1추가 값과 b가 같다면 리턴
    else : return 0,0 # 그냥 아무 값이나 리턴
    
def main():
    A,B = map(int,sys.stdin.readline().split())
    result_a, result_count = dfs(A,B,1) # 시작 값도 세아려주므로 count는 1로 넣어준다
    if result_a == B : print(result_count) # 리턴된 값이 B와 같다면 count 출력
    else : print(-1)

main()

''' 
dfs 실행 추가 설명
1. 두 상황 전부 다 보며 돈다
2. 재귀함수를 돌다가 b값보다 크거나 같다면 그 값(크거나 같은 값)을 리턴
3. 리턴된 값이 b와 같다면 계속해서 리턴하여 처음으로 돌아온다
'''
