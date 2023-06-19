
# J (a,b) -> 두 집합 a,b 사이의 유사도
# 두 집합의 교집합의 크기를 두 집합의 합집합 크기로 나눈 값
# 모두 공집합일 경우 나눗셈이 정의되지 않아 J(a,b) = 1로 정의

from collections import Counter
def solution(str1, str2):
    str1_counter = Counter([(str1[i] + str1[i + 1]).lower() for i in range(len(str1) - 1) if (str1[i].isalpha() and str1[i+1].isalpha())])
    str2_counter = Counter([(str2[i]+str2[i+1]).lower() for i in range(len(str2)-1) if (str2[i].isalpha() and str2[i+1].isalpha())])
    inter,union = len(list((str1_counter & str2_counter).elements())), len(list((str1_counter | str2_counter).elements()))
    if inter ==0 and union == 0:
        return 65536
    else:
        return int(inter/union * 65536)
    # str1_set, str2_set = [], []
    # for i in range(len(str1) - 1):
    #     data = str1[i]+str1[i+1]
    #     str1_set.append(data)
    #     if data in str1_set:
    #         data +=str(str1_set.count(data)+1)
    #     str1_clone.append(data)
    #
    # for i in range(len(str2) - 1):
    #     data = str2[i]+str2[i+1]
    #     str2_set.append(data)
    #     if data in str2_set:
    #         data +=str(str2_set.count(data)+1)
    #     str2_clone.append(data)


str1= "handshake"
str2 = "shake hands"
print(solution(str1,str2))
