# 문제이해를 블로그 통해서 함..
#메모리 :31256 시간 :40
n = int(input())
map = input()

gift = 0
for i in range(1, n):
    if map[i - 1] == "E" and map[i] == "W":
        gift += 1
print(gift)
