
# 개인정보 수집 유효기간
# 모든 달은 28일까지 있음
# 각 기간에 -1일을 한 것이 만기일
# 0일인 경우 -> 이전달 28일

def solution(today, terms, privacies):
    answer = []
    data_set = {}
    for term in terms:
        key,value = term.split(" ")
        data_set[key] = value
    today_list = list(map(int,today.split(".")))
    # 일자 환산 값
    today_data = today_list[0]*12*28 + today_list[1]*28 + today_list[2]

    for i in range(len(privacies)):
        if find(today_data,data_set,privacies[i]):
            answer.append((i+1))
    return answer

def find(today_data,data_set,privacie):
    p,k = privacie.split(" ") # 기간,약관 종류
    p_list = list(map(int,p.split(".")))
    p_list[1]+=int(data_set[k])
    p_data = p_list[0]*12*28 + p_list[1]*28 + p_list[2]

    if p_data <= today_data:
        return True
    else:
        return False


today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today,terms,privacies))