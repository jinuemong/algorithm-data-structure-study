

# 옹알이
# 조카는 "aya", "ye", "woo", "ma" 4가지 발음 구사
# 연속해서 같은 발음 못함
good_data = {"aya", "ye", "woo", "ma"}
bad_data = {"ayaaya", "yeye", "woowoo", "mama"}
def solution(babbling):
    answer = 0
    for baby in babbling:
        answer+=find(baby)
    return answer
def find(baby):
    i = 0
    while i<len(baby):
        if i+2 <= len(baby) and baby[i:i+2] in good_data:
            if i+4 <= len(baby) and baby[i:i+4] in bad_data:
                return 0
            else:
                i+=2
        elif i+3 <= len(baby) and baby[i:i+3] in good_data:

            if i+6 <= len(baby) and baby[i:i+6] in bad_data:
                return 0
            else:
                i+=3
        else:
            break
    if i == len(baby):
        print(baby)
        return 1
    else:
        return 0

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))