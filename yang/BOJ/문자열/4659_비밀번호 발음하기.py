import sys

vowelSet = {'a','e','i','o','u'}
while True:
    s = sys.stdin.readline().strip()
    if s == "end":
        break
    case1 = False # case1 - 모음 하나도 없는 경우 체크
    vCheck = 0 # case2 - 모음 개수 체크
    cCheck = 0 # case2 - 자음 개수 체크
    for i in range(len(s)):
        if i!=0 and s[i] != "e" and s[i] != "o" and s[i-1]==s[i]: #case3 - 연속 체크
            print(f"<{s}> is not acceptable.")
            break
        if s[i] in vowelSet:
            vCheck += 1
            cCheck = 0
            case1 = True
        else:
            cCheck += 1
            vCheck = 0
        if vCheck >= 3 or cCheck >= 3:
            print(f"<{s}> is not acceptable.")
            break
    else:
        if case1:
            print(f"<{s}> is acceptable.")
        else:
            print(f"<{s}> is not acceptable.")