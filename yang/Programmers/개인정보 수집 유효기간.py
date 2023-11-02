def timeConvert(t) :
    year, month, day = map(int, t.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    term_dict = dict()
    today = timeConvert(today)
    answer = []    
    
    for term in terms :
        name, period = term.split()
        term_dict[name] = int(period) * 28
    
    for idx, privacy in enumerate(privacies) :
        start, name = privacy.split()
        end = timeConvert(start) + term_dict[name]
        if end <= today :
            answer.append(idx+1)    
    
    return answer


'''
def solution(today, terms, privacies):
    answer = []
    termsDict = dict()
    today = list(map(int, today.split(".")))
    for t in terms:
        a, b = t.split()
        termsDict[a] = int(b)
    for i, p in enumerate(privacies):
        date, pType = p.split()
        result = appendDate(list(map(int, date.split("."))), termsDict[pType])
        if compareDate(today, result):
            answer.append(i + 1)
    return answer

def appendDate(date, addMonth):
    y, m, d = date
    y += (m + addMonth) // 12
    m = (m + addMonth) % 12
    if m == 0: m = 12
    d -= 1
    if d == 0:
        m -= 1
        if m == 0:
            y -= 1
            m = 12
        d = 28
    return [y, m, d]

def compareDate(today, compare): # 오늘이 지났으면 True
    if today[0] > compare[0]: return True
    if today[1] > compare[1]: return True
    return today[2] > compare[2]
    
'''
today = "2019.12.09"
terms = ["A 12"]
privacies = ["2018.12.10 A", "2010.10.10 A"]

# today = "2020.10.12"
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))