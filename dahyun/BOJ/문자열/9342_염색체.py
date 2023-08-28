# 31256KB/	40ms
'''
문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
(1) 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
(2) 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
(3) 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
(4) 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다
'''
import sys
input = sys.stdin.readline
def result(testcase):
    A,F,C,L = 0,0,0,0 # A : (1) , F : (2) , C : (3) , L : (4)
    for i in range(len(testcase)):
        if testcase[i] == 'A' and A==0: A=1; continue # A가 한번도 나온 적 없고 현재 A일 때 
        
        elif testcase[i] == 'F' and A==1 and F!=1 and testcase[i-1]!='A': F=0; break # A 다음 처음으로 나온 F이지만, F 바로 전이 A가 아님 : False
        elif testcase[i] == 'F' and A==1 : F=1; continue # A 다음 처음으로 나온 F

        elif testcase[i] == 'C' and F==1 and C!=1 and testcase[i-1]!='F': C=0;break # F 다음 처음으로 나온 C이지만, 바로 전이 F가 아님 : False
        elif testcase[i] == 'C' and F==1: C=1; continue # F 다음 처음으로 나온 C
        
        elif A==1 and C==1 and F==1 and L==0 : L=1; continue # A->F->C 순으로 나왔고, 마지막 알파벳이 나옴
        elif A==1 and C==1 and F==1 and L==1 : L=2; break # 마지막 알파벳이 나왔음에도(L) 또 뒤에 알파벳이 존재 : Fasle

    if A==1 and F==1 and C==1 and (L==0 or L==1): return "Infected!"
    else: return "Good"
    
    
for _ in range(int(input())):
    print(result(input()))
