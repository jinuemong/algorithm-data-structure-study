
# J (a,b) -> 두 집합 a,b 사이의 유사도
# 두 집합의 교집합의 크기를 두 집합의 합집합 크기로 나눈 값
# 모두 공집합일 경우 나눗셈이 정의되지 않아 J(a,b) = 1로 정의
import re
def solution(str1, str2):
    str1_set  = set( [re.sub(r"[^a-zA-Z]","",(str1[i]+str1[i+1]).lower()) for i in range(len(str1)-1)])
    str2_set  = set( [re.sub(r"[^a-zA-Z]","",(str2[i]+str2[i+1]).lower()) for i in range(len(str2)-1)])
    print(str1_set)
    print(str2_set)
    print((str1_set&str2_set))
    print((str1_set | str2_set))
    if len(str1_set) == 0 and len(str2_set) == 0:
        return 1
    else:
        return int(( len(str1_set&str2_set) / len(str1_set|str2_set) )*65536)

str1= "handshake"
str2 = "shake hands"
print(solution(str1,str2))
