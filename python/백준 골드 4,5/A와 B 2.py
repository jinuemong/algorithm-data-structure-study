# fun 1: 문자열 뒤에 A 추가
# fun 2: 문자열 뒤에 B 추가 + 문자열 뒤집기

# -> 거꾸로 생각
# fun 1: 문자열 뒤에 A 제거
# fun 2: 문자열 뒤집기, 문자열 뒤에 B 제거
result = 0
def find_result(s,t):
    global result
    if t == s:
        result = 1

    elif len(t)>0:
        if t[-1] == "A":
            find_result(s,t[:-1])
        t_reverse = t[::-1]
        if t_reverse[-1] == "B":
            find_result(s,t_reverse[:-1])

s = input()
t = input()
find_result(s,t)
print(result)