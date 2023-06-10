
# 문자열 나누기 2 시도

def solution(s):
    answer = 0
    count_x, count_y, x,i = 1, 0, s[0], 1
    while i < len(s):
        if s[i] == x:
            count_x+=1
        else:
            count_y+=1

        if count_x == count_y:
            answer+=1
            if i == len(s)-1:
                break
            count_x ,count_y,x= 1,0,s[i+1]
            i+=1
        i+=1
    if count_x != count_y:
        answer+=1


    return answer


s = "aaabbaccccabba"
print(solution(s))