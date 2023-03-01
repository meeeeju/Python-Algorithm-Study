# 31256KB /	488ms
import sys
input = sys.stdin.readline

ecology = {}
try:
    while True:
        tree = input().rstrip()
        if not tree:    # 빈 문자열인 경우 종료
            break
        if tree in ecology.keys():  # 기존에 tree 가 이미 있다면
            ecology[tree]+=1
        else:       # 새로운 tree 라면
            ecology[tree] = 1
except EOFError:
    pass

ecology =dict(sorted(ecology.items()))
ecology_value = ecology.values()
total = sum(ecology_value)

percentage = list(map(lambda x: round((x/total)*100,4),ecology_value))  

result = zip(ecology.keys(),percentage)
for a,b in result:
    print("{0} {1:.4f}".format(a, b))





