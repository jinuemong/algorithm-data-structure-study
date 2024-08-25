
def solution(t, p):
    answer = 0
    i ,n= 0, len(p)
    while  i+n<= len(t):
        if int(t[i:i+n]) <= int(p):
            answer+=1
        i+=1
    return answer

t = "500220839878"
p = "7"
print(solution(t,p))