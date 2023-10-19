# 테스트 9 ~ 테스트 16 시간초과
# 로컬 변수 어떻게 써야할지 모르겠어서 검색해봄 -> nonlocal
# 디버깅 하느라 중간부터는 vscode에서 함

def solution(users, emoticons):
    answer = [0, 0]
    case = []
    def calcul_sale_cases(x, m): # 이모티콘 할인 경우의수 계산
        nonlocal case
        if len(case)==m:
            if case == [0, 0, 2, 0]:
                pass
            nonlocal answer
            new_ans = calcul_ans(case)
            answer = compare_ans(answer, new_ans)
            return
        for i in range(x, m):
            for j in range(4):
                case.append(j)
                calcul_sale_cases(x+1, m)
                case.pop()
    def calcul_ans(case):
        sale = [40, 30, 20, 10]
        ans = [0]*2
        users_sum = [0]*len(users)
        for e in range(len(case)):
            for u in range(len(users)):
                if users_sum[u] == -1:
                    continue
                if users[u][0] <= sale[case[e]]: # 구매
                    users_sum[u] += emoticons[e] * (100-sale[case[e]]) * 0.01
                    if users_sum[u] >= users[u][1]: # 이모티콘 플러스 구매
                        ans[0] += 1
                        users_sum[u] = -1
        for s in users_sum:
            if s > 0:
                ans[1] += s
        ans[1] = int(ans[1])
        return ans
    def compare_ans(before_ans, new_ans):
        if before_ans[0] > new_ans[0]:
            return before_ans
        elif new_ans[0] > before_ans[0]:
            return new_ans
        else:
            if before_ans[1] > new_ans[1]:
                return before_ans
            else:
                return new_ans

    calcul_sale_cases(0, len(emoticons))
    return answer
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons))