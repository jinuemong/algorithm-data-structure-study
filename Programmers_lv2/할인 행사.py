
# X*Z 마트

# 일정한 금액을 지불하면 10일 동안 회원 자격을 부여
# 한 가지 제품 할인 하는 행사
# 하루에 하나씩만 구매 가능
# 정현이는 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입

def solution(want, number, discount):
    answer = 0
    want_set = set([one*number for one, number in zip(want,number)])
    for i in range(0,len(discount)-9):
        data_set = set([data*(discount[i:i+10].count(data)) for data in discount[i:i+10]])
        if len(want_set -data_set) == 0:
            answer+=1
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
numbers = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana",
            "rice", "apple", "pork", "banana", "pork",
            "rice", "pot", "banana", "apple", "banana"]

print(solution(want,numbers,discount))
