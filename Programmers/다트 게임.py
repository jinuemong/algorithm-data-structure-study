

# 다트 게임

# 다트를 3번 던짐
# 점수의 합계
# s , d, t : 1제곱, 2제곱, 3제곱
# *, # : (해당 점수 + 바로 전 점수)* 2 , 해당 점수 : 마이너스
# *가 처음에 나올 경우 첫 점수만 2배가 됨
# 스타상의 효과는 중첨되며, 중첩된 스타상은 4배가 됨
# 스타상의 효과와 아치상은 중첩되며, 중첩된 아차상은 -2배


def solution(dartResult):
    answer,data_list, i = 0 ,[0], 0
    data_set = {"S":1,"D":2,"T":3,"*":2,"#":-1}
    while i < len(dartResult):
        dart = dartResult[i]
        if dartResult[i:i+2] =="10":
            data_list.append(10)
            i+=1
        elif dart not in data_set:
            data_list.append(int(dart))
        if dart in data_set:
            if dart in {"S","D","T"}:
                data_list[-1] = data_list[-1] ** data_set[dart]
            elif dart == "*":
                data_list[-1]*=2
                data_list[-2] *= 2
            else:
                data_list[-1]*=(-1)
        i+=1
    for data in data_list:
        answer+= data
    return answer

dartResult  = "1S2D*3T"
print(solution(dartResult))