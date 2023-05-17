
# 15785 : 무한 문자열

# f(“abcd”) = “abcdabcdabcdabcd…”

# S = “ababab”, T = “abab”라면 f(S)와 f(T) 모두 “ababababababab…

# 두 문자열이 달라도 무한으로 간다면 같은 문자열이 될 수 있음

# 두 문자열이 주어졌을 때 f(s) = f(t) 를 증명
# 두 문자열의 길이를 같게하여 비교


for t_i in range(int(input())):
    s,t = input().split()
    result = "no"
    if s*len(t) == t*len(s):
        result = "yes"
    print(f"#{t_i+1} {result}")
