def solution(cap, n, deliveries, pickups):
    answer = 0
    end = n - 1

    while end > -1 and deliveries[end] == 0 and pickups[end] == 0:
        end -= 1

    while end > -1:
        delivery = cap
        pick = cap
        answer += end + 1
        for i in range(end, -1, -1): # n-1 ~ 0
            # 배달하기
            if delivery >= deliveries[i]:
                delivery -= deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= delivery
                delivery = 0
            # 수거하기
            if pick >= pickups[i]:
                pick -= pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= pick
                pick = 0
            if delivery == 0 and pick == 0: break
        while end > -1 and deliveries[end] == 0 and pickups[end] == 0:
            end -= 1
    
    return answer * 2


cap, n, deliveries, pickups = 4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]
print(solution(cap, n, deliveries, pickups))