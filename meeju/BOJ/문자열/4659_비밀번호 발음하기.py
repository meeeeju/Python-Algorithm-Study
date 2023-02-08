import sys
input = sys.stdin.readline

password=input().rstrip()
vowels = ['a','e','i','o','u']
has_vowels=False
triple_vowelss=0
triple_consonants=0
printed=False

while(password != 'end'):
    # print(password)
    triple_vowelss=0
    triple_consonants=0
    printed=False
    has_vowels=False
    prev_s='e'
    for s in password:
        if prev_s==s :
            if prev_s=='o' or  prev_s=='e':
                pass
            else:
                print("<{}> is not acceptable.".format(password))
                printed=True
                break
        if s in vowels:
            triple_vowelss+=1
            triple_consonants=0
            has_vowels=True
        else:
            triple_vowelss=0
            triple_consonants+=1
        if triple_consonants >=3 or triple_vowelss >=3:
            print("<{}> is not acceptable.".format(password))
            printed=True
            break
        prev_s=s
    if not printed:
        if  not has_vowels:
            print("<{}> is not acceptable.".format(password))
        else:
            print("<{}> is acceptable.".format(password))
    password=input().rstrip()
    


'''

#풀이과정
모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다. -> has_vowels 변수로 모음 여부를 체크해줌

모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다. ->  triple_vowelss=0, triple_consonants=0 변수를 이용하여 연속으로 3개 오는지 체크해줌

같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다. ->  prev_s='e' 변수를 두어 이전 문자와 비교해줌

# 입력
a
tv
ptoui
bontres
zoggax
wiinq
eep
houctuh
end

#출력
<a> is acceptable.
<tv> is not acceptable.
<ptoui> is not acceptable.
<bontres> is not acceptable.
<zoggax> is not acceptable.
<wiinq> is not acceptable.
<eep> is acceptable.
<houctuh> is acceptable.
'''