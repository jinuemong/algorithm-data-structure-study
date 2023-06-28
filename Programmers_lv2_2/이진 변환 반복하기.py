

# 이진 변환 반복하기


def solution(s):
    zero , count = 0,0
    while len(s)>1:
        count+=1
        s_len =  len(s)
        s= s.replace("0","")
        zero+=(s_len - len(s))
        s = trans(len(s))
    return [count,zero]

def trans(s):
    data = ""
    while s > 0:
        data = str(s%2) + data
        s = s//2
    return data

s = "110010101001"
print(solution(s))
