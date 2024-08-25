
# 숫자 짝꿍

def solution(X, Y):
    answer = ''
    x_set = {9:0,8:0,7:0,6:0,5:0,4:0,3:0,2:0,1:0,0:0}
    y_set = {9:0,8:0,7:0,6:0,5:0,4:0,3:0,2:0,1:0,0:0}
    for x_i in list(X):
        x_set[int(x_i)]+=1
    for y_i in list(Y):
        y_set[int(y_i)]+=1

    for i in range(9,-1,-1):
        answer+= min(x_set[i],y_set[i])*str(i)
    if len(answer)==0:
        return '-1'
    elif answer[0]=='0':
        return '0'
    else:
        return ''.join(sorted(answer,reverse=True))

x = "100"
y = "2345"
print(solution(x ,y))
