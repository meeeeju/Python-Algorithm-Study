# 블로그 참고

def search(number) : # 재귀 호출을 통해 이진 트리가 가능한지 찾음
    length = len(number)
    if length == 1 or '1' not in number or '0' not in number:
        return True
    
    mid = length // 2 # 중간노드 == 루트노드
    if number[mid] == '0': # 리프노드가 아니므로 자손이 있어야함
        return False
    
    return search(number[:mid]) and search(number[mid+1:])

def solution(numbers):
    # 이진수로 다 변환
    bin_numbers = [ bin(x)[2:] for x in numbers]
    # 포화 이진트리에 맞는 길이 찾기
    for i in range(len(bin_numbers)):
        x = 1
        while True:
            length = 2**x - 1
            if length >= len(bin_numbers[i]):
                bin_numbers[i] = '0'*(length - len(bin_numbers[i])) + bin_numbers[i]
                break
            x += 1
    # 정답 구하기
    answer = []
    for number in bin_numbers :
        answer.append(1 if search(number) else 0)
    
    return answer

numbers = [7, 42, 5]
numbers = [63, 111, 95]
print(solution(numbers))