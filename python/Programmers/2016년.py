
# 2016년
# 1,3,5..: 31
# 4,6... : 30
# 2 : 29
def solution(a, b):
    data_set = {2 : "SUN",3 : "MON",4 : "TUE",
                5 : "WED",6 : "THU",0 : "FRI", 1 : "SAT"}
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    sum  = b - 1
    for  i in range(a-1):
        sum+= months[i]

    return data_set[int(sum%7)]

a = 5
b = 24
print(solution(a,b))