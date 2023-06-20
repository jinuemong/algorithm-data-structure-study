

# J (a,b) -> 두 집합 a,b 사이의 유사도
# 두 집합의 교집합의 크기를 두 집합의 합집합 크기로 나눈 값
# 모두 공집합일 경우 나눗셈이 정의되지 않아 J(a,b) = 1로 정의
import re
def solution(str1, str2):
    str1_set ,str2_set = set(),set()
    for i in range(0,len(str1)-1):
        for j in range(i,len(str1)):
            str1_set.add(re.sub(r"[^a-zA-Z]","",(str1[i]+str1[j]).lower()))
    for i in range(0,len(str2)-1):
        for j in range(i,len(str2)):
            str2_set.add( re.sub(r"[^a-zA-Z]","", (str2[i] + str2[j]).lower()) )
    print(str1_set)
    print(str2_set)
    print((str1_set|str2_set))
    print((str1_set&str2_set))
    answer = 0
    return int((len(str1_set|str2_set) / len(str1_set&str2_set))*65536)


str1= "FRANCE"
str2 = "french"
print(solution(str1,str2))
