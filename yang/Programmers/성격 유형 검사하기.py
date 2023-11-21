def solution(survey, choices):
    scores = calculScore(survey, choices)
    result = calculResult(scores)
    return result

def initScore():
    scores = dict()
    scores["R"] = 0
    scores["T"] = 0
    scores["C"] = 0
    scores["F"] = 0
    scores["J"] = 0
    scores["M"] = 0
    scores["A"] = 0
    scores["N"] = 0
    return scores

def calculScore(survey, choices):
    n = len(survey)
    scores = initScore()
    for i in range(n):
        first, second = survey[i][0], survey[i][1]
        if choices[i] < 4: # 비동의
            scores[first] += 4 - choices[i]
        else: # 동의
            scores[second] += choices[i] - 4
    return scores

def calculResult(score):
    result = ""
    if score["R"] >= score["T"]:
        result += "R"
    else:
        result += "T"
    if score["C"] >= score["F"]:
        result += "C"
    else:
        result += "F"
    if score["J"] >= score["M"]:
        result += "J"
    else:
        result += "M"
    if score["A"] >= score["N"]:
        result += "A"
    else:
        result += "N"
    return result

solution(["TR", "RT", "TR"]	, 	[7, 1, 3])