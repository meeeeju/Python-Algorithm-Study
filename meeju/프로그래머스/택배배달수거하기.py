# 그리디
def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    
    d = 0 # delivery
    p = 0 # pickup
    
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0: # 둘 중 하나라도 수거할게 있다면
            d -= cap
            p -= cap
            answer += (n - i) * 2
    return answer