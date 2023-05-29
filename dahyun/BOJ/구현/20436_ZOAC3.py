# 31256 KB / 44 ms
def check(n):  # x,y 구하는 함수
    for i in range(3):
        for j in range(len(keyboard[i])):
            if n==keyboard[i][j] : return i,j
keyboard=[['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]
consonant=['q','w','e','r','t','a','s','d','f','g','z','x','c','v']  # 자음
vowel= ['y','u','i','o','p','h','j','k','l','b','n','m']  # 모음
sl,sr = input().split()  # 성수의 왼쪽 검지, 오른쪽 검지가 있는 문자
string = input().strip()  # 성우가 입력해야하는 문자열

result=0
sx1,sy1 = check(sl)  # 성우의 왼쪽 검지의 위치
sx2,sy2 = check(sr)  # 성우의 오른쪽 검지의 위치
for s in string:
    x,y = check(s)  # 입력해야하는 문자 하나의 위치
    if s in consonant :  # 문자가 자음이면 성우의 왼쪽 검지가 움직여야 함
        result+=abs(sx1-x)+abs(sy1-y)+1
        sx1,sy1 = x,y
    elif s in vowel : # 문자가 모음이면 성우의 오른쪽 검지가 움직여야 함
        result+=abs(sx2-x)+abs(sy2-y)+1
        sx2,sy2 = x,y
print(result)
