# 31256	56

import sys
input = sys.stdin.readline

'''
sequence subsequence
person compression
VERDI vivaVittorioEmanueleReDiItalia
caseDoesMatter CaseDoesMatter'''

def Ispartofword(s, t): # s : 부분 문자열 t : 문자열
    j = 0

    for i in range(len(t)):
        if t[i] == s[j]:
            j +=1
            if j == len(s):
                return True
    else:
        return False

while True:
    try:
        s, t = input().split()
        
        if Ispartofword(s,t):
            print("Yes")
        else:
            print("No")
    except:
        break
    


