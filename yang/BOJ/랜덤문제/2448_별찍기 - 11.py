# 55448KB / 240ms

N = int(input())
stars = [[] for _ in range(11)] # stars[k][i] == k일때 모양의 i 번째 줄
# 초기값
stars[0].append("  *  ")
stars[0].append(" * * ")
stars[0].append("*****")

# k 값 구하기
k = 0
n = N // 3
while n >= 2:
    n = n // 2
    k += 1

# k 까지 별 만들기
for i in range(1, k + 1):
    # 삼각형 윗부분 만들기
    size = len(stars[i - 1][0])
    space_count = ((size * 2 + 1) - size) // 2
    space = " " * space_count
    for s in stars[i - 1]:
        stars[i].append(space + s + space)
    
    # 삼각형 아래부분 만들기
    for s in stars[i - 1]:
        stars[i].append(s + " " + s)

# 만들어진 별 출력하기
for s in stars[k]:
    print(s)