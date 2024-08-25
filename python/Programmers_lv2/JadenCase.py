

# JadenCase

def solution(s):
    check, s = False,list(s)
    for i in range(len(s)):
        if s[i]==" ":
            check = True
        elif (s[i] != " " and check) or i==0:
            check = False
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()

    return "".join(s)

print(solution("3people unFollowed me"))