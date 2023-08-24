# 31256KB / 40ms
# 질문게시판 반례 참고
from sys import stdin
sinput = stdin.readline

address = sinput().rstrip()
ans = []
replace_index = -1
temp = ""
i = 0
while i<len(address):
    if address[i]==":":
        if address[i+1]==":":
            if temp != "":
                ans.append("0"*(4-len(temp))+temp)
                temp = ""
            replace_index = len(ans)
            i += 1
        else:
            ans.append("0"*(4-len(temp))+temp)
            temp = ""
    else:
        temp += address[i]
    i += 1
if temp != "":
    ans.append("0"*(4-len(temp))+temp)
    temp = ""
if replace_index != -1:
    for _ in range(8-len(ans)):
        ans.insert(replace_index, "0000")
print(':'.join(ans))
