# 31256 KB / 92 ms
import sys
input = sys.stdin.readline
fibonacci=[0,1]+[0 for _ in range(44)]  # 피보나치 45는 1,000,000,000을 넘지 않음
def fibo_check(n):  # n보다 작은 피보나치 찾기
    for i in range(2,46):
        fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
        if fibonacci[i]==n: return fibonacci[i] # 만약 피보나치[i]가 n이라면 피보나치[i]값 반환
        elif fibonacci[i]>n: return fibonacci[i-1]  # 만약 피보나치[i]가 n보다 크다면 피보나치[i-1]값 반환

for _ in range(int(input())):
    n=int(input())
    llist = []  # 피보나치 값들 저장하는 리스트
    while True:  # n이 0이 될 때까지 반복
        ch=fibo_check(n)  # ch : 피보나치 값이 n이거나 n보다 작은 값 
        llist.append(ch)
        n=n-ch  # n에서 n보다 작은 ch 빼기
        if n==0: break  
    print(* reversed(llist)) # 큰 값부터 저장이 되므로 거꾸로 뒤집에서 출력
